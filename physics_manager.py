from physics_cube import PhysicsCube

physics = {
	"cube" : PhysicsCube
}

def handle_physics(new_physics):
	return physics[new_physics]

def copy_physics(new_physics, old_physics):
	new_physics.a = old_physics.a
	new_physics.v = old_physics.v
	new_physics.x = old_physics.x