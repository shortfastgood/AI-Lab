import bpy
import random
from math import radians

def clear_scene():
    bpy.ops.object.select_all(action='DESELECT')
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False)

def create_fidget_sphere(name, radius, location):
    bpy.ops.mesh.primitive_uv_sphere_add(radius=radius, location=location)
    sphere = bpy.context.active_object
    sphere.name = name
    return sphere

def apply_random_rotation(obj, rotation_range=(-45, 45)):
    random_rotation = (
        radians(random.uniform(rotation_range[0], rotation_range[1])),
        radians(random.uniform(rotation_range[0], rotation_range[1])),
        radians(random.uniform(rotation_range[0], rotation_range[1]))
    )
    obj.rotation_euler = random_rotation

def create_fidget_rings(sphere, num_rings=4):
    rings = []
    for i in range(num_rings):
        bpy.ops.mesh.primitive_torus_add(
            align='WORLD', location=sphere.location, rotation=(radians(90), 0, radians(360 / num_rings * i)),
            major_radius=sphere.dimensions.x + i * 0.1, minor_radius=0.05)
        ring = bpy.context.active_object
        ring.name = f"Ring_{i}"
        apply_random_rotation(ring)
        rings.append(ring)
    return rings

def animate_obj(obj, start_frame, end_frame, rotation_axis, angle_per_frame):
    bpy.context.view_layer.objects.active = obj
    obj.select_set(True)
    bpy.context.scene.frame_start = start_frame
    bpy.context.scene.frame_end = end_frame
    bpy.context.scene.frame_current = start_frame

    bpy.ops.anim.keyframe_insert_menu(type='Rotation')
    for frame in range(start_frame + 1, end_frame + 1):
        bpy.context.scene.frame_current = frame
        obj.rotation_euler[rotation_axis] += radians(angle_per_frame)
        bpy.ops.anim.keyframe_insert_menu(type='Rotation')

def animate_fidget_rings(rings, start_frame, end_frame, angle_per_frame):
    for i, ring in enumerate(rings):
        rotation_axis = i % 3
        animate_obj(ring, start_frame, end_frame, rotation_axis, angle_per_frame)

if __name__ == "__main__":
    clear_scene()
    sphere = create_fidget_sphere("FidgetSphere", 1, (0, 0, 0))
    rings = create_fidget_rings(sphere)
    animate_fidget_rings(rings, 1, 100, 3)
