import curses

import color

from screen import Screen

from tile_map import *

class StatScreen(Screen):
	def __init__(self, stdscr):
		super().__init__(stdscr)

		stats_window = curses.newwin(20, 20, 1, 1)

		stats_window.addstr(0, 0, f"Highest score: ")
		stats_window.addstr(2, 0, f"Games played: ")
		stats_window.addstr(4, 0, f"(R)eturn: ")

		self.add_windows([stats_window])


	def handle_input(self):
		key = self.pop_input()

		while key is not None:
			key = key.lower()

			if key == 'r':
				self.clear_inputs()
				return self.change_window("main")
			elif key == 'q':
				exit()

			key = self.pop_input()