import dgl
import networkx as nx
import trimesh
import trimesh.graph
import os
import torch
import _pickle as pickle
import numpy as np
import queue


def mesh2dgl(path, save=False):
    mesh = trimesh.load_mesh(path)
    graph = trimesh.graph.vertex_adjacency_graph(mesh)
    dgl_graph = dgl.DGLGraph()
    dgl_graph.from_networkx(graph)
    dgl_graph.ndata['l'] = torch.Tensor(mesh.vertices)

    print(nx.is_connected(graph))

    # for i in range(len(mesh.vertices)):
    #     if mesh.vertices[i].all() != dgl_graph.nodes[i].data['l'].numpy()[0].all():
    #         print("{} != {}".format(mesh.vertices[i], dgl_graph.nodes[i].data['l'][0].numpy()))
    print("Original graph has", len(graph.edges), "edges.")
    print("Original mesh has", len(mesh.faces), "faces.")
    if save:
        out_path = save_path(path, ".dgl")
        save_file(out_path, dgl_graph)
    return dgl_graph


def dgl2mesh(path, save=False):
    in_file = open(path, "rb")
    graph = pickle.load(in_file)
    g = graph.to_networkx(node_attrs='l').to_undirected()
    print(nx.is_connected(g))

    print("G has", len(g.edges()), "edges.")

    mesh = trimesh.Trimesh()
    mesh.vertices = graph.ndata['l']
    # TODO: Add triangles, BFS
    n_nodes = len(graph.nodes())
    traversed = [False] * n_nodes
    count = 0
    if n_nodes <= 0:
        print("Warning: Void mesh!")
        return mesh
    q = queue.Queue()
    q.put(0)

    faces = []

    while count < n_nodes:
        if not q.empty():
            crt_node = q.get()
        else:
            for i, b in enumerate(traversed):
                if not b:
                    crt_node = i
                    break
        neighbor_list = list(g.neighbors(crt_node))
        for i, n1 in enumerate(neighbor_list):
            if traversed[n1] or n1 == crt_node:
                continue
            q.put(n1)

            for j in range(i+1, len(neighbor_list)):
                n2 = neighbor_list[j]
                if g.has_edge(n1, n2) and n2 != crt_node:
                    faces.append([crt_node, n1, n2])
        traversed[crt_node] = True
        count += 1
    mesh.faces = np.array(faces)
    print("end")
    
    print(mesh.faces)
    in_file.close()
    mesh.show()
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
    path = "./model_normalized.obj"
    graph = mesh2dgl(path, save=True)
    # graph_path = "./model_normalized.dgl"
    # mesh = dgl2mesh(graph_path)
    