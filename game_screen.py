import curses

import color

from collections import deque

from screen import Screen

from tile_map import *

N_ROWS = 20
N_COLUMNS = 60

START_Y = 1
START_X = 10

## del later
import random
##

class GameScreen(Screen):
	def __init__(self, stdscr):
		super().__init__(stdscr)
		
		# Y, X
		self.old_pos = [START_Y, START_X]
		self.new_pos = self.old_pos
		self.alive = True

		# Score tracking
		self.score = 0;

		self.arrays = []
		self.arrays.append(deque([1] * N_COLUMNS))
		'''
		self.arrays = [deque([0] * N_COLUMNS) for _ in range(N_ROWS - 1)]
		'''
		for i in range(0, N_ROWS - 2):
			self.arrays.append(deque([0] * N_COLUMNS))
		self.arrays.append(deque([1] * N_COLUMNS))

		self.tile_maps = [TileMap(map_data=list(array), codes={0: 0x2800, 1: 0x2591, 2: 0x2756, 3: 0x2731}) for array in self.arrays]
		self.ground = len(self.arrays) - 1

		# Each line of the game window will be a string
		#
		# call write_window() to write deque contents to window
		#
		# call superclass self.refresh() to display contents

		game_window = curses.newwin(len(self.arrays) + 1, len(self.arrays[0]) + 2, 1, 1)
		menu_window = curses.newwin(6, 20, 1, len(self.arrays[0]) + 2)

		self.game_window = game_window
		self.menu_window = menu_window

		self.add_windows([game_window, menu_window])

		self.write_window()


	def write_window(self):
		for index, array in enumerate(self.arrays):
			self.game_window.addstr(index, 0, f"{self.tile_maps[index].string}", color.colors['GAME'])

		self.menu_window.addstr(0, 0, f"Score: {self.score}")
		self.menu_window.addstr(2, 0, f"(Q)uit")
		self.menu_window.addstr(4, 0, f"(R)eturn")



	def handle_input(self):
		if not self.alive:
			return self.change_window("death")

		key = self.pop_input()

		while key is not None:
			key = key.lower()

			print(key)

			if key == 'k': # Down

				## 
				## IN THIS SECTION, CHECK SURROUNDINGS
				##

				if self.old_pos[0] < N_ROWS - 2:
					self.new_pos = [self.old_pos[0] + 1, self.old_pos[1]]
				self.clear_inputs()
				return None
				
			elif key == 'l': # Up

				## 
				## IN THIS SECTION, CHECK SURROUNDINGS
				##

				if self.old_pos[0] > 1:
					self.new_pos = [self.old_pos[0] - 1, self.old_pos[1]]
				self.clear_inputs()
				return None

			elif key == 'r':
				self.clear_inputs()
				return self.change_window("main")
			elif key == 'q':
				exit()

			key = self.pop_input()

	def tick(self):
		# Create the trail. Set the old position to the trail character
		self.arrays[N_ROWS - self.old_pos[0] - 1][self.old_pos[1]] = 2
		self.tile_maps[N_ROWS - self.old_pos[0] - 1].update_map(self.arrays[N_ROWS - self.old_pos[0] - 1])

		##
		## IN THIS SECTION, CALCULATE NEW POSITION AND
		## CHECK COLLISION
		##

		## RANDOM GEN

		for i in range(1, N_ROWS - 1):
			array = self.arrays[i]

			array.popleft()
			array.append(random.choices([0, 1], weights=[90, 10])[0])

			self.tile_maps[i].update_map(array)

		# Check new position. If it's a collision, load the new screen
		if self.arrays[N_ROWS - self.new_pos[0] - 1][self.new_pos[1]] == 1:
			# Write to death buffer
			self.write_buffer("death", [self.score])
			self.alive = False

			# Increment stats buffer
			stats_buffer = self.read_buffer("stats")
			if self.score > stats_buffer[0]:
				stats_buffer[0] = self.score
			stats_buffer[1] += 1
			self.write_buffer("stats", stats_buffer)
			
			return


		self.arrays[N_ROWS - self.new_pos[0] - 1][self.new_pos[1]] = 3
		self.tile_maps[N_ROWS - self.new_pos[0] - 1].update_map(self.arrays[N_ROWS - self.new_pos[0] - 1])


		self.old_pos = [self.new_pos[0], self.new_pos[1]]

		self.write_window()
		self.increase_score()

	def increase_score(self):
		self.score += 1

	def get_score(self):
		return self.score