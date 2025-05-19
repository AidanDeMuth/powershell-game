import curses

colors = {}

def init_colors():
	curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_GREEN)
	curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_MAGENTA)
	curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

	colors['TITLE_TERMINAL'] = curses.color_pair(1)
	colors['TITLE_DASH'] = curses.color_pair(2)
	colors['GAME'] = curses.color_pair(3)