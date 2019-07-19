import trimesh
import open3d
from trimesh import sample
import numpy as np


def sample_surface(in_path, out_path, count_v):
    mesh = trimesh.load_mesh(in_path)
    vertices, faces = sample.sample_surface_even(mesh, count_v)
    normals = mesh.face_normals[faces]
    dist = np.random.randn(len(vertices)) * normals
    vertices = vertices + dist
    # save mesh, and normal vectors
    f = open(out_path, "w")
    for item in vertices:
        f.write("{} {} {} {}\n".format(vertices[0], vertices[1], vertices[2], dist))
    f.close()


def reconstruct_sdf(sdf):
    pass


if __name__ == "__main__":
    in_path = "./data/cube.obj"
    out_path = "./data/cube.xyz"
    sample_surface(in_path, out_path, 1000)
