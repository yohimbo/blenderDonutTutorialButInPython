import bpy 
from math import * 

# create donut initial state
bpy.ops.mesh.primitive_torus_add(major_segments=40,minor_segments=16,major_radius=0.91,minor_radius=0.61)
