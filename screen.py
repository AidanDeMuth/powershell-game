import sys
import bisect

from collections import deque

from tile_map import *

# GENERIC SCREEN CLASS
#
# Any subclass should create windows and maps within the constructor
# It is also necessary to override input handlers
# A new instance of a screen should have full functionality

class Screen:
	# For now process inputs like a queue, maybe change later
	def __init__(self, stdscr):
		stdscr.clear()
		stdscr.refresh()

		self.inputs = deque()
		self.stdscr = stdscr
		self.windows = []

	## WINDOW MANAGER
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

	## INPUT MANAGER
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

	def handle_input(self): # OVERRIDE
		pass

	def tick(self):
		pass