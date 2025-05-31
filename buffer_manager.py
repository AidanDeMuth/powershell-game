'''
buffer_manager.py

Module used to store global states of a screen. Can be written and read to by any screen by calling
self.read_buffer() or self.write_buffer(). See screen.py for more details.
'''

buffers = {
	"stats" : [0, 0], # games played, top score
	"death" : [], # score
}

def read_buffer(buffer_name):
	return buffers[buffer_name].copy()

def write_buffer(buffer_name, data):
	buffers[buffer_name] = data.copy()