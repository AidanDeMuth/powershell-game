import sys
import bisect

from collections import deque

from tile_map import *

import buffer_manager

'''
GENERIC SCREEN CLASS

Implements basic functionality of window management, input management, global buffer management,
and game ticks. A game tick is a "frame," or rather the point where new position or state is calculated.

- Any subclass should be fully initialized in it's constructor, meaning windows and maps.
- It is also necessary to override input handlers to allow for navigation of screens
'''

class Screen:
	def __init__(self, stdscr):
		stdscr.clear()
		stdscr.refresh()

		# Every screen, regardless of what it does, will take from stdin and maintain windows
		self.inputs = deque()
		self.stdscr = stdscr
		self.windows = []

	'''
	WINDOW MANAGEMENT

	Each screen maintains a list of windows, which are iterated over and refreshed every event loop. It is best to add them
	in the order they appear
	'''

	def add_window(self, window=None):
		if window is None:
			raise ValueError

		self.windows.append(window)

	def add_windows(self, windows=None): # list of windows
		if windows is None:
			raise ValueError

		for i in windows:
			self.windows.append(i)

	def remove_window(self, window=None):
		if window is None:
			raise ValueError

		self.windows.remove(window)

	def change_window(self, screen):
		return screen

	def refresh(self):
		for i in self.windows:
			i.refresh()

	def clear(self):
		self.stdscr.clear()

	'''
	ÍNPUT MANAGEMENT

	All received inputs every event loop are processed to the current screen's buffer in a queue.
	Overriding handle_input() is necessary to give each screen it's own functionality

	- For custom input handling these can be overridden
	'''

	def add_input(self, key_input):
		self.inputs.append(key_input)

	def pop_input(self):
		return self.inputs.pop() if self.inputs else None

	def print_inputs(self):
		print(f"Num elements in deque: {len(self.inputs)}")
		for item in self.inputs:
			print(item, end='')
		print("\nFlush")

	def clear_inputs(self):
		self.inputs.clear()

	def handle_input(self):
		pass

	'''
	STATE MANAGEMENT
	tick() is an optional function that will run each event loop that will update the state of the game.
	Override to change the state of a screen.

	write_buffer() - Given a buffer name and data, will write to the global buffers. Can be dynamic or static
	read_buffer() - Given a buffer name, will return a copy of the global buffer stored by that name	
	'''

	def tick(self):
		pass

	def write_buffer(self, buffer_name, data):
		buffer_manager.write_buffer(buffer_name, data)

	def read_buffer(self, buffer_name):
		return buffer_manager.read_buffer(buffer_name)