import curses

import color

from screen import Screen

from tile_map import *

class DeathScreen(Screen):
	def __init__(self, stdscr):
		super().__init__(stdscr)

		# Get last game data
		game_stats = self.read_buffer("death")

		death_window = curses.newwin(20, 20, 1, 1)

		death_window.addstr(0, 0, f"You died")
		death_window.addstr(2, 0, f"Your Score: {game_stats[0]}")
		death_window.addstr(4, 0, f"(R)eturn")
		death_window.addstr(6, 0, f"(P)lay again")
		death_window.addstr(8, 0, f"(Q)uit")

		self.add_windows([death_window])

	def handle_input(self):
		key = self.pop_input()

		while key is not None:
			key = key.lower()

			if key == 'r':
				self.clear_inputs()
				return self.change_window("main")
			elif key == 'p':
				self.clear_inputs()
				return self.change_window("game")
			elif key == 'q':
				exit()

			key = self.pop_input()