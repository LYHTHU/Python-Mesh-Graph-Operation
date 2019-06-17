import dgl
import networkx as nx
import trimesh
import os

def mesh2dgl(path, save=False):
    mesh = trimesh.load_mesh(path)
    graph = trimesh.graph.vertex_adjacency_graph(mesh)
    
    return graph

def dgl2mesh(path, save=False):
    pass

def save_path(origin, suffix):
    breakpoint = origin.rfind('/')
    dir_path = origin[:breakpoint]
    name = origin[breakpoint:origin.rfind('.')]+suffix
    save_path = os.path.join(dir_path+name)
    return save_path


if __name__ == "__main__":
    path = "./model_normalized.obj"
    # g = mesh2dgl(path, save=True)
