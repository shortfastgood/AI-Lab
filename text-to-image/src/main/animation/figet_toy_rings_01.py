import bpy
import math

# Clear all existing mesh objects
bpy.ops.object.select_all(action='DESELECT')
bpy.ops.object.select_by_type(type='MESH')
bpy.ops.object.delete()

# Function to create a ring
def create_ring(name, radius, thickness, location, rotation):
    bpy.ops.mesh.primitive_torus_add(
        align='WORLD', major_radius=radius, minor_radius=thickness
    )
    ring = bpy.context.active_object
    ring.name = name
    ring.location = location
    ring.rotation_euler = rotation
    return ring

# Create three rings for the fidget toy
ring1 = create_ring(
    "Ring1", radius=2, thickness=0.2, location=(0, 0, 0), rotation=(0, 0, 0)
)
ring2 = create_ring(
    "Ring2", radius=2, thickness=0.2, location=(0, 0, 0), rotation=(math.pi / 2, 0,     0)
)
ring3 = create_ring(
    "Ring3", radius=2, thickness=0.2, location=(0, 0, 0), rotation=(0, math.pi / 2,     0)
)

# Set up the rotation animation
frame_start = 1
frame_end = 250
rotation_speed = 2 * math.pi / (frame_end - frame_start)

bpy.context.scene.frame_start = frame_start
bpy.context.scene.frame_end = frame_end

# Animate the rotation
for frame in range(frame_start, frame_end + 1):
    bpy.context.scene.frame_set(frame)
    ring1.rotation_euler.z += rotation_speed
    ring2.rotation_euler.x += rotation_speed
    ring3.rotation_euler.y += rotation_speed
    ring1.keyframe_insert(data_path="rotation_euler", frame=frame)
    ring2.keyframe_insert(data_path="rotation_euler", frame=frame)
    ring3.keyframe_insert(data_path="rotation_euler", frame=frame)

print("Fidget toy created.")