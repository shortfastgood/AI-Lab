import bpy
import mathutils
import random

# Function to create a new point light
def create_point_light(name, location, radius, power):
    light_data = bpy.data.lights.new(name=name, type='POINT')
    light_data.energy = power
    light_data.shadow_soft_size = radius

    light_object = bpy.data.objects.new(name=name, object_data=light_data)
    light_object.location = location
    bpy.context.collection.objects.link(light_object)
    return light_object

# Create a new material
def create_wood_material(name):
    material = bpy.data.materials.new(name)
    material.use_nodes = True
    bsdf_node = material.node_tree.nodes["Principled BSDF"]

    # Add noise texture node
    noise_texture_node = material.node_tree.nodes.new("ShaderNodeTexNoise")
    noise_texture_node.inputs["Scale"].default_value = 10

    # Add color ramp node
    color_ramp_node = material.node_tree.nodes.new("ShaderNodeValToRGB")
    color_ramp_node.color_ramp.elements[0].color = (0.4, 0.25, 0.1, 1)  # Dark wood color
    color_ramp_node.color_ramp.elements[1].color = (0.7, 0.45, 0.2, 1)  # Light wood color

    # Connect nodes
    material.node_tree.links.new(bsdf_node.inputs["Base Color"], color_ramp_node.outputs["Color"])
    material.node_tree.links.new(color_ramp_node.inputs["Fac"], noise_texture_node.outputs["Fac"])

    return material

# Create a new cube with the specified dimensions
def create_cube(name, dimensions):
    bpy.ops.mesh.primitive_cube_add(size=1)
    cube = bpy.context.active_object
    cube.name = name
    cube.dimensions = dimensions
    return cube

def create_wooden_lath(name,x,y,z,material):
    lath = create_cube(name,(x,y,z))
    lath.data.materials.append(material)
    return lath

def create_long_face(name, offset):

    bench_l = bpy.types.Scene.bench_l
    bench_h = bpy.types.Scene.bench_h
    bench_w = bpy.types.Scene.bench_w

    lath_hl = bpy.types.Scene.lath_hl
    lath_w = bench_w - 2 * lath_hl
    leg = bpy.types.Scene.bench_leg
    material = bpy.types.Scene.wood_material

    # horizontal laths
    lath1 = create_wooden_lath(name + "_lath_1", lath_w, lath_hl, lath_hl, material)
    if offset >= 0:
        lath1.location.y = offset - lath_hl/2
    else:
        lath1.location.y = offset + lath_hl/2
    lath1.location.z = bench_h - lath_hl/2
    lath2 = create_wooden_lath(name + "_lath_2", lath_w, lath_hl, lath_hl, material)
    if offset >= 0:
        lath2.location.y = offset - lath_hl/2
    else:
        lath2.location.y = offset + lath_hl/2
    lath2.location.z = leg + lath_hl/2

    # external legs
    lath3 = create_wooden_lath(name + "_lath_3", lath_hl, lath_hl, bench_h, material)
    lath3.location.x = lath_w/2 + lath_hl/2
    if offset >= 0:
        lath3.location.y = offset - lath_hl/2
    else:
        lath3.location.y = offset + lath_hl/2
    lath3.location.z = bench_h * 0.5

    lath4 = create_wooden_lath(name + "_lath_4", lath_hl, lath_hl, bench_h, material)
    lath4.location.x = -lath_w/2 - lath_hl/2
    if offset >= 0:
        lath4.location.y = offset - lath_hl/2
    else:
        lath4.location.y = offset + lath_hl/2
    lath4.location.z = bench_h * 0.5

    # central lath
    z = bench_h - leg - 2 * lath_hl
    lath5 = create_wooden_lath(name + "_lath_5", lath_hl, lath_hl, z, material)
    if offset >= 0:
        lath5.location.y = offset - lath_hl/2
    else:
        lath5.location.y = offset + lath_hl/2
    lath5.location.z = leg + z/2 + lath_hl

    # central leg
    lath6 = create_wooden_lath(name + "_lath_6", lath_hl, lath_hl, leg, material)
    if offset >= 0:
        lath6.location.y = offset - lath_hl/2
    else:
        lath6.location.y = offset + lath_hl/2
    lath6.location.z = leg/2

    # mid lath
    z = bench_h - leg - 2 * lath_hl
    lath7 = create_wooden_lath(name + "_lath_7", lath_hl, lath_hl, z, material)
    lath7.location.x = (lath_w/2 + lath_hl/2)/2
    if offset >= 0:
        lath7.location.y = offset - lath_hl/2
    else:
        lath7.location.y = offset + lath_hl/2
    lath7.location.z = leg + z/2 + lath_hl

    # mid leg
    lath8 = create_wooden_lath(name + "_lath_8", lath_hl, lath_hl, leg, material)
    lath8.location.x = (lath_w/2 + lath_hl/2)/2
    if offset >= 0:
        lath8.location.y = offset - lath_hl/2
    else:
        lath8.location.y = offset + lath_hl/2
    lath8.location.z = leg/2

    # mid lath
    z = bench_h - leg - 2 * lath_hl
    lath9 = create_wooden_lath(name + "_lath_9", lath_hl, lath_hl, z, material)
    lath9.location.x = (lath_hl/2 - bench_w/2)/2
    if offset >= 0:
        lath9.location.y = offset - lath_hl/2
    else:
        lath9.location.y = offset + lath_hl/2
    lath9.location.z = leg + z/2 + lath_hl

    # mid leg
    lathA = create_wooden_lath(name + "_lath_A", lath_hl, lath_hl, leg, material)
    lathA.location.x = (lath_hl/2 - bench_w/2)/2
    if offset >= 0:
        lathA.location.y = offset - lath_hl/2
    else:
        lathA.location.y = offset + lath_hl/2
    lathA.location.z = leg/2

def create_short_face(name, offset):

    bench_l = bpy.types.Scene.bench_l
    bench_h = bpy.types.Scene.bench_h
    bench_w = bpy.types.Scene.bench_w

    lath_hl = bpy.types.Scene.lath_hl
    lath_w = bench_l - 2 * lath_hl
    leg = bpy.types.Scene.bench_leg
    material = bpy.types.Scene.wood_material

    laths = []
    for i in range(8):
        lath = create_wooden_lath(name + "_lath_" + str(i), lath_hl, lath_w, lath_hl, material)
        laths.append(lath)


    # central
    laths[0].location.z = leg + lath_hl/2

    # side
    laths[1].location.x = bench_w/2 - lath_hl/2
    laths[1].location.z = bench_h - lath_hl/2

    laths[2].location.x = lath_hl/2 - bench_w/2
    laths[2].location.z = bench_h - lath_hl/2

    # side
    laths[3].location.x = bench_w/2 - lath_hl/2
    laths[3].location.z = leg + lath_hl/2

    laths[4].location.x = lath_hl/2 - bench_w/2
    laths[4].location.z = leg + lath_hl/2

    # mid
    laths[5].location.x = (bench_w/2 - lath_hl/2)/2
    laths[5].location.z = leg + lath_hl/2

    # mid
    laths[6].location.x = (lath_hl/2 - bench_w/2)/2
    laths[6].location.z = leg + lath_hl/2

    laths[7].location.z = bench_h - lath_hl/2

def create_ground_plate():

    # Define the dimensions of the GroundPlate
    x=bpy.types.Scene.bench_w
    y=bpy.types.Scene.bench_l
    z=0.05

    # Define the center of the GroundPlate
    center = mathutils.Vector((0, -10, bpy.types.Scene.bench_leg + bpy.types.Scene.lath_hl))

    # Create a new mesh for the GroundPlate
    mesh = bpy.data.meshes.new('GroundPlate')

    # Define the vertices of the GroundPlate
    verts = [
        center + mathutils.Vector((-x/2, -y/2, 0)),
        center + mathutils.Vector((x/2, -y/2, 0)),
        center + mathutils.Vector((x/2, y/2, 0)),
        center + mathutils.Vector((-x/2, y/2, 0)),
        ]

    # Define the faces of the GroundPlate
    faces = [
        (0, 1, 2, 3),
    ]

    # Add the vertices and faces to the mesh
    mesh.from_pydata(verts, [], faces)

    # Update the mesh and create a new object
    mesh.update()
    obj = bpy.data.objects.new('GroundPlate', mesh)

    # Add the object to the scene
    scene = bpy.context.scene
    if obj is not None and obj.name not in scene.collection.objects:
        scene.collection.objects.link(obj)

    # Set the mass of the GroundPlate
    if obj is not None and obj.rigid_body is not None:
        obj.rigid_body.mass = sum((x, y, z))
    else:
        print("Error: Could not set mass. GroundPlare or rigid body not found.")

    obj.data.materials.append(bpy.types.Scene.wood_material)


bpy.types.Scene.lath_hl = 0.58

bpy.types.Scene.bench_l = 8
bpy.types.Scene.bench_h = 5
bpy.types.Scene.bench_w = 25 + 2 * bpy.types.Scene.lath_hl

bpy.types.Scene.bench_leg = 0.4

# Set up scene
bpy.ops.object.select_all(action='DESELECT')
bpy.ops.object.select_by_type(type='MESH')
bpy.ops.object.delete()

bpy.ops.object.select_by_type(type='LIGHT')
bpy.ops.object.delete()

# Create a point light and position it
point_light = create_point_light("New_Point_Light", (-2, -5, 10), 1, 5000)

# Create wooden material
bpy.types.Scene.wood_material = create_wood_material("Wood")

# Skeleton
create_long_face("front_skeleton", -bpy.types.Scene.bench_l/2)
create_long_face("back_skeleton", bpy.types.Scene.bench_l/2)
create_short_face("right_skeleton", -bpy.types.Scene.bench_w/2)
create_short_face("left_skeleton", bpy.types.Scene.bench_w/2)

create_ground_plate()

bpy.ops.object.select_all(action='DESELECT')
