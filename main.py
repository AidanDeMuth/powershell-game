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

FRAMES_PER_SECOND = 10
TIME_PER_FRAME = (1.0 / FRAMES_PER_SECOND) * (1000)

sys.stdout.reconfigure(encoding='utf-8')

def main(stdscr):
	color.init_colors()
	
	curses.curs_set(0)
	
	lines = curses.LINES;
	columns = curses.COLS;

	curr_screen = MainScreen(stdscr)
	


	## EVENT LOOP ##
	last_time = time.perf_counter() * 1000

	while True:
		## CAPTURE INPUTS HERE

		if msvcrt.kbhit():
			key = msvcrt.getch().decode('utf-8')
			print(key)

			curr_screen.add_input(key)

		## EVENT HANDLER

		curr_time = time.perf_counter() * 1000

		if curr_time - last_time >= TIME_PER_FRAME:

			event = curr_screen.handle_input()

			if event:
				new_screen = handle_screen(new_screen=event, stdscr=stdscr)

				if isinstance(new_screen, Screen):
					print("Screen")
					curr_screen = new_screen

			last_time = curr_time

			curr_screen.tick() ## EVERY FRAME IS A TICK

		## REFRESH

		curr_screen.clear()
		curr_screen.refresh()


if __name__ == "__main__":
	curses.wrapper(main)
