# Test loading 3D mesh obj file.

import trimesh
import pymesh
import networkx as nx

mesh_path = "model_normalized.obj"

def load_mesh(path):
    mesh = trimesh.load(path)
    print(mesh)
    mesh.show()

# TODO: need to be figure out 

def create_ellisoid():
    mesh = trimesh.Trimesh(vertices=[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0]],
                       faces=[[0, 1, 2], [0, 1, 3], [0, 2, 3], [1, 2, 3]])

    return mesh


def simple_deformation(obj):
    pass

def mesh2graph(mesh):
    graph = trimesh.graph.vertex_adjacency_graph(mesh)
    return graph

def test_mesh2graph():
    mesh = trimesh.load(mesh_path)
    graph = mesh2graph(mesh)


if __name__ == "__main__":
    # obj = create_ellisoid()
    # simple_deformation(obj)
        
    test_mesh2graph()


