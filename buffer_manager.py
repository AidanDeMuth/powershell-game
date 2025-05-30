buffers = {
	"stats" : [0, 0], # games played, top score
	"death" : [], # score
}

def read_buffer(buffer_name):
	return buffers[buffer_name].copy()

def write_buffer(buffer_name, data):
	buffers[buffer_name] = data.copy()