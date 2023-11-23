# Blender Donut Tutorial But In Python
The classic [Blender Guru](https://www.youtube.com/channel/UCOKHwx1VCdgnxwbjyb9Iu1g) tutorial but entirely in a python script.

This is the creation of a juicy, overflowing donut :doughnut: in the classic blender tutorial manner. The big difference is here it is made entirely by script rather than by mouse or by tablet.

Why? Why not? But also - shouldn't we be able to treat blender models and environments the same way we treat our code - by saving it in stages and states in git?

If you can script it, script it.

# The code

```python
import bpy 
from math import *
```

Import the blender python [package](https://pypi.org/project/bpy/) and math because it always comes up. 

First we set the donut :doughnut: settings to initial state. A fat donut :doughnut: as Blender Guru states: 

```python
bpy.ops.mesh.primitive_torus_add(major_segments=40,minor_segments=16,major_radius=0.91,minor_radius=0.61)```
```

* Major Segments, Number of segments for the main ring of the torus :ox:
* Minor Segments, Number of segments for the minor ring of the torus :ox:
* Major Radius, Radius from the origin to the center of the cross sections
* Minor Radius, Radius of the torus’ cross section

Next we need to select the object to begin working with it so we have donut!!!!
`donut = bpy.context.active_object`
