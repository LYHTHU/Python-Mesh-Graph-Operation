import numpy as np
import mcubes
import trimesh
import sys

  
# Create a data volume (100 x 100 x 100)
X, Y, Z = np.mgrid[-1:1:100j, -1:1:100j, -1:1:100j]

X, Y, Z = X.ravel().reshape(-1, 1), Y.ravel().reshape(-1, 1), Z.ravel().reshape(-1, 1)
input_xyz = np.concatenate((X, Y, Z), axis=1)
# print(input_xyz)
X, Y, Z = input_xyz[:, 0], input_xyz[:, 1], input_xyz[:, 2], 
X, Y, Z = np.reshape(X, (100, 100, 100)), np.reshape(Y, (100, 100, 100)), np.reshape(Z, (100, 100, 100))


u = np.sign( (X)**2 + (Y)**2 + (Z)**2 - 0.1**2 )
# u = (X)**2 + (Y)**2 + (Z)**2 - 0.1**2
u = np.sign((X)**2 + (Y)**4 + (Z)**5 - 0.04)
# Extract the 0-isosurface
vertices, triangles = mcubes.marching_cubes(u, 0)
vertices = (vertices - 50) / 100
  
# Export the result to sphere.dae
mesh = trimesh.Trimesh(vertices=vertices, faces=triangles)
mesh.export("sphere.off")