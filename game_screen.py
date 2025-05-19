import curses

import color

from collections import deque

from screen import Screen

from tile_map import *

N_ROWS = 20
N_COLUMNS = 60

class GameScreen(Screen):
	def __init__(self, stdscr):
		super().__init__(stdscr)
		self.x_pos = 6
		self.y_pos = 1
		
		self.arrays = []
		self.arrays.append(deque([1] * N_COLUMNS))
		'''
		self.arrays = [deque([0] * N_COLUMNS) for _ in range(N_ROWS - 1)]
		'''
		for i in range(0, N_ROWS - 2):
			self.arrays.append(deque([0] * N_COLUMNS))
		self.arrays.append(deque([1] * N_COLUMNS))

		self.tile_maps = [TileMap(map_data=list(array), codes={0: 0x2800, 1: 0x2591}) for array in self.arrays]
		self.ground = len(self.arrays) - 1

		# Each line of the game window will be a string
		#
		# call write_window() to write deque contents to window
		#
		# call superclass self.refresh() to display contents

		game_window = curses.newwin(len(self.arrays) + 3, len(self.arrays[0]) + 2, 1, 1)
		self.game_window = game_window
		self.add_windows([game_window])

		self.write_window()


	def write_window(self):
		for index, array in enumerate(self.arrays):
			self.game_window.addstr(index, 0, f"{self.tile_maps[index].string}", color.colors['GAME'])


	def handle_input(self):
		key = self.pop_input()

		while key is not None:
			key = key.lower()

			if key == ' ':

				## 
				## IN THIS SECTION, CHECK SURROUNDINGS
				## AND APPLY THE VELOCITY AND ACCELERATION
				##

				self.clear_inputs()
				return None
				##  

			elif key == 'r':
				self.clear_inputs()
				return self.change_window("main")
			elif key == 'q':
				exit()

			key = self.pop_input()

	def tick(self):
		self.arrays[N_ROWS - self.y_pos - 1][self.x_pos] = 0

		##
		## IN THIS SECTION, CALCULATE NEW POSITION AND
		## CHECK COLLISION
		##



		for index, array in enumerate(self.arrays):
			array.popleft()
			array.append(1)

			self.tile_maps[index].update_map(array)

		self.arrays[N_ROWS - self.y_pos - 1][self.x_pos] = 1
		self.tile_maps[N_ROWS - self.y_pos - 1].update_map(self.arrays[N_ROWS - self.y_pos - 1])

		self.write_window()