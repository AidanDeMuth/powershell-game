import curses

import color

from collections import deque

from screen import Screen

from tile_map import *

class GameScreen(Screen):
	def __init__(self, stdscr):
		super().__init__(stdscr)

		self.arrays = [
			deque([0, 0, 0, 0, 0, 0, 0]),
			deque([0, 0, 0, 0, 0, 0, 0]),
			deque([0, 0, 0, 0, 0, 0, 0]),
			deque([0, 0, 0, 0, 0, 0, 0]),
			deque([0, 0, 0, 0, 0, 0, 0]),
			deque([0, 0, 0, 0, 0, 0, 0]),
			deque([0, 0, 0, 0, 0, 0, 0]),
			deque([0, 0, 0, 0, 0, 0, 0]),
			deque([0, 0, 0, 0, 0, 0, 0]),
			deque([0, 0, 0, 0, 0, 0, 0]),
			deque([0, 0, 0, 0, 0, 0, 0]),
			deque([0, 0, 0, 0, 0, 0, 0]),
			deque([0, 0, 0, 0, 0, 0, 0]),
			deque([0, 0, 0, 0, 0, 0, 0]),
			deque([0, 0, 0, 0, 0, 0, 0]),
			deque([0, 0, 0, 0, 0, 0, 0]),
			deque([1, 1, 1, 1, 1, 1, 1])
		]
		self.tile_maps = [TileMap(map_data=list(array)) for array in self.arrays]
		self.ground = len(self.arrays) - 1

		# Each line of the game window will be a string
		#
		# call write_window() to write deque contents to window
		#
		# call superclass self.refresh() to display contents

		game_window = curses.newwin(len(self.arrays) + 5, len(self.arrays[0]) + 4, 1, 1)
		self.game_window = game_window
		self.add_windows([game_window])

		self.write_window()
		self.refresh()


	def write_window(self):
		for index, array in enumerate(self.arrays):
			self.game_window.addstr(index, 0, f"{self.tile_maps[index].string}", color.colors['GAME'])


	def handle_input(self):
		key = self.pop_input()

		while key is not None:
			key = key.lower()

			if key == ' ':
				return None
				##  

			elif key == 'r':
				return self.change_window("main")
			elif key == 'q':
				exit()

			key = self.pop_input()