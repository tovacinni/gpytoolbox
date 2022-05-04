import numpy as np
from context import gpytoolbox
import igl
import polyscope as ps

# Load mesh
V, F = igl.read_triangle_mesh("unit_tests_data/bunny_oded.obj")
V = gpytoolbox.normalize_points(V)
v, q = gpytoolbox.build_octree_as_hex_mesh(V)

t = gpytoolbox.libigl_hex_to_polyscope_hex(q)
ps.init()
ps_vol = ps.register_volume_mesh("test volume mesh", v, hexes=t)
ps.show()