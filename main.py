import os
import sys
import time
import math
import msvcrt
import time

import curses
import color

from tile_map import *

from screen import *
from screen_manager import *

'''
main.py

Engine for the game, runs an event loop ideally once every frame
'''

FRAMES_PER_SECOND = 20 # Modify this line to change the framerate

TIME_PER_FRAME = (1.0 / FRAMES_PER_SECOND) * (1000)

sys.stdout.reconfigure(encoding='utf-8')

def main(stdscr):
	color.init_colors()
	
	curses.curs_set(0)
	
	lines = curses.LINES;
	columns = curses.COLS;

	# Only one screen can be active at a time, so initialize it to your home screen
	curr_screen = MainScreen(stdscr)

	## EVENT LOOP ##
	last_time = time.perf_counter() * 1000

	while True:
		## CAPTURE INPUTS HERE

		if msvcrt.kbhit():
			key = msvcrt.getch().decode('utf-8')
			curr_screen.add_input(key)

		## EVENT HANDLER

		curr_time = time.perf_counter() * 1000

		if curr_time - last_time >= TIME_PER_FRAME:
			# Input event
			event = curr_screen.handle_input()

			if event:
				new_screen = handle_screen(new_screen=event, stdscr=stdscr)

				if isinstance(new_screen, Screen):
					curr_screen = new_screen


			# Game tick event
			curr_screen.tick()
			last_time = curr_time

		# Redraw screens
		curr_screen.clear()
		curr_screen.refresh()


if __name__ == "__main__":
	curses.wrapper(main)
