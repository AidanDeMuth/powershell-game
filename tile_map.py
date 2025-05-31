import math

'''
tile_map.py

Creates a mapping UTF codes to a N different codes.
'''
class TileMap:
	def __init__(self, codes={0: 0x2800, 1: 0x2588, 2: 0x2591}, map_name=None, map_data=None, rows=1):
		if map_data is None:
			raise ValueError("No map data provided!")

		self.name = map_name
		self.raw_map = map_data
		self.num_rows = rows
		self.row_length = int(len(self.raw_map) / self.num_rows)
		self.utf_map = None
		self.string = None
		self.codes = codes;

		self.update_utf_data()

	# Sets a new buffer to the entire map
	def update_map(self, new_map):
		self.raw_map = new_map
		self.update_utf_data()

	# Converts each numeric value to it's UTF value
	def update_utf_data(self):
		self.utf_map = [] 
		self.string = ""

		for i in self.raw_map:
			self.utf_map += chr(self.codes[i])
			self.string += str(chr(self.codes[i]))
