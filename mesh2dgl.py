import dgl
import networkx as nx
import trimesh
import os
import torch
import _pickle as pickle
import numpy as np

def mesh2dgl(path, save=False):
    mesh = trimesh.load_mesh(path)
    graph = trimesh.graph.vertex_adjacency_graph(mesh)
    dgl_graph = dgl.DGLGraph()
    dgl_graph.from_networkx(graph)
    dgl_graph.ndata['l'] = torch.Tensor(mesh.vertices)

    # for i in range(len(mesh.vertices)):
    #     if mesh.vertices[i].all() != dgl_graph.nodes[i].data['l'].numpy()[0].all():
    #         print("{} != {}".format(mesh.vertices[i], dgl_graph.nodes[i].data['l'][0].numpy()))


    if save:
        out_path = save_path(path, ".dgl")
        save_file(out_path, dgl_graph)
    return dgl_graph


def dgl2mesh(path, save=False):
    in_file = open(path, "rb")
    graph = pickle.load(in_file)

    mesh = trimesh.Trimesh(vertices=graph.ndata["l"])
    # print(graph.nodes[:].data['l'].numpy())
    # print(graph.ndata["l"].numpy())
    # print(mesh.vertices[:])

    # Add triangle 
    in_file.close()
    return mesh

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
    # path = "./model_normalized.obj"
    # graph = mesh2dgl(path, save=True)
    graph_path = "./model_normalized.dgl"
    mesh = dgl2mesh(graph_path)
