import trimesh
from trimesh import sample, proximity
import numpy as np
import open3d
import time
from show_pcd import *

def sample_near_surface(in_path, out_path, count_v, ratio=0.02):
    mesh = trimesh.load_mesh(in_path)
    vertices, faces = sample.sample_surface(mesh, count_v)

    # Using mesh.scale(the length of the diagonal of the axis aligned bounding box) of the mesh
    normals = mesh.face_normals[faces] # unit vectors, length = 1
    rand = ratio*mesh.scale* np.random.randn(len(vertices), 1)
    vertices = vertices + rand*normals

    # rand = ratio*mesh.scale*np.random.random((count_v, 3))
    # vertices = vertices + rand

    distance = proximity.signed_distance(mesh, vertices).reshape(-1, 1)
    vertices = np.hstack((vertices, distance))
    # save mesh, and normal vectors
    # Using numpy
    np.save(out_path, vertices)




if __name__ == "__main__":
    start = time.time()
    in_path = "./data/model_normalized.off"
    out_path = "./data/model_normalized.npy"
    sample_near_surface(in_path, out_path, 2000)
    end = time.time()
    print("Using {} seconds.".format(end-start))
    show_pcd(out_path)
