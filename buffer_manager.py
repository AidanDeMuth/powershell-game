buffers = {
	"stats" : [],
	"death" : [],
}

def clear_buffer(buffer):
	buffers[buffer].clear()

def fetch_buffer(buffer):
	return buffers[buffer].copy()

def set_buffer(buffer, data):
	buffers[buffer] = data.copy()