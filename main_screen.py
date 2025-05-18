import curses

import color

from screen import Screen

from tile_map import TileMap

# left right top bottom, top left right, bottom left right
main_border = [
	chr(0x25A2), 
	chr(0x25A2),
	chr(0x25A2),
	chr(0x25A2),
	chr(0x25A9), 
	chr(0x25A9), 
	chr(0x25A9),
	chr(0x25A9)
]

main_border = [
	'|', 
	'|',
	'-',
	'-',
	'+', 
	'+', 
	'+',
	'+'
]

# 5 rows for title
terminal_map_1 = [1, 1, 1, 2, 0, 1, 1, 1, 2, 0, 1, 1, 1, 2, 0, 1, 1, 1, 1, 1, 2, 0, 1, 1, 1, 2, 0, 1, 2, 0, 1, 2, 0, 0, 1, 2, 0, 0, 1, 2, 0]
terminal_map_2 = [0, 1, 2, 0, 0, 1, 2, 0, 0, 0, 1, 2, 1, 2, 0, 1, 2, 1, 2, 1, 2, 0, 0, 1, 2, 0, 0, 1, 1, 2, 1, 2, 0, 1, 2, 1, 2, 0, 1, 2, 0]
terminal_map_3 = [0, 1, 2, 0, 0, 1, 1, 1, 2, 0, 1, 1, 1, 2, 0, 1, 2, 1, 2, 1, 2, 0, 0, 1, 2, 0, 0, 1, 2, 1, 1, 2, 0, 1, 1, 1, 2, 0, 1, 2, 0]
terminal_map_4 = [0, 1, 2, 0, 0, 1, 2, 0, 0, 0, 1, 1, 2, 0, 0, 1, 2, 1, 2, 1, 2, 0, 0, 1, 2, 0, 0, 1, 2, 0, 1, 2, 0, 1, 2, 1, 2, 0, 1, 2, 0]
terminal_map_5 = [0, 1, 2, 0, 0, 1, 1, 1, 2, 0, 1, 2, 1, 2, 0, 1, 2, 1, 2, 1, 2, 0, 1, 1, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 1, 2, 0, 1, 1, 1]
terminal_map_raw = terminal_map_1 + terminal_map_2 + terminal_map_3 + terminal_map_4 + terminal_map_5

dash_map_1 = [1, 1, 2, 0, 0, 0, 1, 2, 0, 0, 1, 1, 1, 2, 0, 1, 2, 1, 2]
dash_map_2 = [1, 2, 1, 2, 0, 1, 2, 1, 2, 0, 1, 2, 0, 0, 0, 1, 2, 1, 2]
dash_map_3 = [1, 2, 1, 2, 0, 1, 1, 1, 2, 0, 1, 1, 1, 2, 0, 1, 1, 1, 2]
dash_map_4 = [1, 2, 1, 2, 0, 1, 2, 1, 2, 0, 0, 0, 1, 2, 0, 1, 2, 1, 2]
dash_map_5 = [1, 1, 2, 0, 0, 1, 2, 1, 2, 0, 1, 1, 1, 2, 0, 1, 2, 1, 2]
dash_map_raw = dash_map_1 + dash_map_2 + dash_map_3 + dash_map_4 + dash_map_5


class MainScreen(Screen):
	def __init__(self, stdscr):
		super().__init__(stdscr)
		
		terminal_map = None
		dash_map = None

		try:
			terminal_map = TileMap(codes={0: 0x2800, 1: 0x2588, 2: 0x2591}, map_data=terminal_map_raw, rows=5)
			dash_map = TileMap(codes={0: 0x2800, 1: 0x2588, 2: 0x2591}, map_data=dash_map_raw, rows=5)
		except Exception as e:
			print(f"Error creating map object: \n {e}")
			exit(1)

		main_window = curses.newwin(terminal_map.num_rows + dash_map.num_rows + 6, 
								terminal_map.row_length + 4, 
								1, 1)
		main_window.border(*main_border)

		terminal_window = curses.newwin(terminal_map.num_rows + 1, terminal_map.row_length, 3, 3)
		terminal_window.addstr(0, 0, f"{terminal_map.string}", color.colors['TITLE_TERMINAL']) # Relative to window

		dash_window = curses.newwin(dash_map.num_rows + 1, dash_map.row_length, 10, 3)
		dash_window.addstr(0, 0, f"{dash_map.string}", color.colors['TITLE_DASH'])
	
		self.add_windows([main_window, terminal_window, dash_window])


	def handle_input(self):
		key = self.pop_input()

		while key is not None:
			key = key.lower()

			if key == 'p':
				return self.change_window("game")
			elif key == 's':
				return self.change_window("stat")
			elif key == 'q':
				exit()

			key = self.pop_input()
				