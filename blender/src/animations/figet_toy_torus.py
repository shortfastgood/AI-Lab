import bpy
import math

# Function to create a torus
def create_torus(name, location, rotation, major_radius, minor_radius):
    bpy.ops.mesh.primitive_torus_add(
        align='WORLD', location=location, rotation=rotation,
        major_radius=major_radius, minor_radius=minor_radius
    )
    torus = bpy.context.active_object
    torus.name = name
    return torus

# Clear existing mesh objects (optional)
bpy.ops.object.select_all(action='DESELECT')
bpy.ops.object.select_by_type(type='MESH')
bpy.ops.object.delete()

# Create three tori
torus_1 = create_torus("Torus1", (0, 0, 0), (0, 0, 0), 2, 0.5)
torus_2 = create_torus("Torus2", (0, 0, 0), (math.radians(90), 0, 0), 2.5, 0.5)
torus_3 = create_torus("Torus3", (0, 0, 0), (0, math.radians(90), 0), 3, 0.5)

# Animate the rotation of the tori
frame_start = 1
frame_end = 250

for obj, axis in zip([torus_1, torus_2, torus_3], ['X', 'Y', 'Z']):
    bpy.context.view_layer.objects.active = obj
    obj.select_set(True)
    
    for frame in range(frame_start, frame_end + 1, 10):
        bpy.context.scene.frame_set(frame)
        obj.rotation_euler.rotate_axis(axis, math.radians(36))  # 36 degrees per frame step
        obj.keyframe_insert(data_path='rotation_euler', frame=frame)

# Set the end frame for the animation
bpy.context.scene.frame_end = frame_end
