import numpy as np
import mcubes
import trimesh
  
# Create a data volume (100 x 100 x 100)
X, Y, Z = np.mgrid[-1:1:100j, -1:1:100j, -1:1:100j]
u = np.sign( (X)**2 + (Y)**2 + (Z)**2 - 0.1**2 )
# u = (X)**2 + (Y)**2 + (Z)**2 - 0.1**2
# Extract the 0-isosurface
vertices, triangles = mcubes.marching_cubes(u, 0)
  
# Export the result to sphere.dae
mesh = trimesh.Trimesh(vertices=vertices, faces=triangles)
mesh.export("sphere.off")