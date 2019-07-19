import trimesh
from trimesh import sample
import numpy as np

import time


def sample_surface(in_path, out_path, count_v):
    mesh = trimesh.load_mesh(in_path)
    vertices, faces = sample.sample_surface_even(mesh, count_v)
    normals = mesh.face_normals[faces]
    # TODO: figure out how to choose the distance of sampling points
    rand = np.random.randn(len(vertices), 1)
    dist = rand * normals
    vertices = vertices + dist
    # save mesh, and normal vectors
    f = open(out_path, "w")
    for i, item in enumerate(vertices):
        f.write("{} {} {} {}\n".format(item[0], item[1], item[2], np.sign(i)*np.linalg.norm(dist[i])))
    f.close()


def reconstruct_sdf(sdf):
    # TODO: reconstruct surface based on SDF
    raise NotImplementedError


def sphere(x, y, z, r=5):
    return x**2 + y**2 + z**2 - r**2


if __name__ == "__main__":
    start = time.time()
    in_path = "./data/model_normalized.obj"
    out_path = "./data/model_normalized.xyz"
    sample_surface(in_path, out_path, 2000)
    end = time.time()
    print("Using {} seconds.".format(end-start))
