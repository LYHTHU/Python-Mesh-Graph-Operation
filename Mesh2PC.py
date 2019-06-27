import trimesh
from mesh2dgl import *

"""
    Convert mesh or dgl graph to point cloud
"""


def mesh2PC(mesh):
    raise NotImplementedError


def dgl2PC(graph):
    mesh = dgl2mesh("", graph)
    return mesh2PC(mesh)