import trimesh
import open3d
from mesh2dgl import *

"""
    Convert mesh or dgl graph to point cloud
"""

def load_pcd(path):
    pcd = open3d.io.read_point_cloud(path)
    return pcd

def mesh2pcd(path="", obj=None, save=False):
    mesh = obj
    if not obj:
        mesh = open3d.io.read_triangle_mesh(path)
    



def dgl2PC(graph):
    mesh = dgl2mesh("", graph)
    return mesh2pcd(mesh)


if __name__ == "__main__":
    # path = "./data/ankylosaurus_mesh.ply"
    # pcd = load_pcd(path)
    # print(np.asarray(pcd.points))
    # open3d.visualization.draw_geometries([pcd])
    path = "./data/model_normalized.obj"
    mesh2pcd(path=path)