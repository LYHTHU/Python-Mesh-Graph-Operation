# Test loading 3D mesh obj file.

import trimesh
import pymesh
import networkx as nx
import matplotlib.pyplot as plt 
import torch

mesh_path = "model_normalized.obj"

def load_mesh(path):
    mesh = trimesh.load(path)
    print(mesh)
    mesh.show()

# TODO: need to be figure out 

def create_ellisoid():
    mesh = trimesh.primitives.Capsule()
    # mesh = trimesh.primitives.Extrusion()
    mesh.show()
    return mesh

def simple_deformation(obj):
    pass

def mesh2graph(mesh):
    graph = trimesh.graph.vertex_adjacency_graph(mesh)
    return graph

def test_mesh2graph():
    mesh = trimesh.load_mesh(mesh_path)
    graph = mesh2graph(mesh)

    # for v in mesh.vertices:
    #     print(v)


if __name__ == "__main__":
    # obj = create_ellisoid()
    # simple_deformation(obj)      
    # test_mesh2graph()
    create_ellisoid()


