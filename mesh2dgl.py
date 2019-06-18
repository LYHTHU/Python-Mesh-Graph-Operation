import dgl
import networkx as nx
import trimesh
import os
import torch
import _pickle as pickle

def mesh2dgl(path, save=False):
    mesh = trimesh.load_mesh(path)
    graph = trimesh.graph.vertex_adjacency_graph(mesh)
    dgl_graph = dgl.DGLGraph()
    dgl_graph.from_networkx(graph)
    dgl_graph.ndata['l'] = torch.Tensor(mesh.vertices)
    out_path = save_path(path, ".dgl")
    save_file(out_path, dgl_graph)
    return dgl_graph


def dgl2mesh(path, save=False):
    pass

def save_path(origin, suffix):
    breakpoint = origin.rfind('/')
    dir_path = origin[:breakpoint]
    name = origin[breakpoint:origin.rfind('.')]+suffix
    save_path = os.path.join(dir_path+name)
    return save_path

def save_file(out_path, obj):
    output = open(out_path, "wb")
    pickle.dump(obj, output)
    output.close()

if __name__ == "__main__":
    path = "./model_normalized.obj"
    graph = mesh2dgl(path, save=True)
