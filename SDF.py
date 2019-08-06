import trimesh
from trimesh import sample, proximity
import numpy as np
import open3d
import time


def sample_near_surface(in_path, out_path, count_v, ratio=0.02):
    mesh = trimesh.load_mesh(in_path)
    vertices, faces = sample.sample_surface(mesh, count_v)
    normals = mesh.face_normals[faces] # unit vectors, length = 1
    # Using mesh.scale(the length of the diagonal of the axis aligned bounding box) of the mesh
    rand = ratio*mesh.scale* np.random.randn(len(vertices), 1)
    vertices = vertices + rand*normals
    distance = proximity.signed_distance(mesh, vertices).reshape(-1, 1)
    vertices = np.hstack((vertices, distance))
    # save mesh, and normal vectors
    # Using numpy
    np.save(out_path, vertices)

def show_pcd(path):
    print("Showing {}".format(path))
    raw = np.load(path)
    arr = raw[:, 0:3]
    color = []
    pcd = open3d.geometry.PointCloud()
    for i in range(raw[:, 3].size):
        if raw[i, 3] > 0:
            color.append([1, 0, 0])
        else:
            color.append([0, 0, 1])
    pcd.points = open3d.utility.Vector3dVector(arr)
    pcd.colors = open3d.utility.Vector3dVector(color)
    open3d.visualization.draw_geometries([pcd])


if __name__ == "__main__":
    start = time.time()
    in_path = "./data/model_normalized.off"
    out_path = "./data/model_normalized.npy"
    sample_surface(in_path, out_path, 2000)
    end = time.time()
    print("Using {} seconds.".format(end-start))
    show_pcd(out_path)
