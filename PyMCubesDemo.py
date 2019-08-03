import numpy as np
import mcubes
import trimesh
  
# Create a data volume (100 x 100 x 100)
X, Y, Z = np.mgrid[-50:50, -50:50, -50:50] / 100
u = (X)**2 + (Y)**3 + (Z)**4 - 0.1**2
  
# Extract the 0-isosurface
vertices, triangles = mcubes.marching_cubes(u, 0)
print(type(vertices), type(triangles))
  
# Export the result to sphere.dae
mesh = trimesh.Trimesh(vertices=vertices, faces=triangles)
mesh.export("sphere.off")