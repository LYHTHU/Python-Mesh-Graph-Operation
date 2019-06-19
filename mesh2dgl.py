import dgl
import networkx as nx
import trimesh
import trimesh.graph
import os
import torch
import _pickle as pickle
import numpy as np
import queue


def mesh2dgl(path, save=False, show = False):
    print("Mesh to DGL")
    mesh = trimesh.load_mesh(path)
    # graph = trimesh.graph.vertex_adjacency_graph(mesh).to_directed()
    # graph.remove_edges_from(list(graph.edges()))
    graph = nx.DiGraph()
    graph.add_edges_from(mesh.edges)

    if show:
        mesh.show()

    print("Original graph has", len(graph.edges), "edges.")
    print("Original mesh has", len(mesh.faces), "faces.")
    # Why unique edges are even less than edges.
    print("Original mesh has", len(mesh.vertices), "vertices.")
    # print("Original mesh has", len(mesh.edges_unique), "unique edges.")    
    dgl_graph = dgl.DGLGraph()
    dgl_graph.from_networkx(graph)
    print("DGL graph has ", dgl_graph.number_of_edges(), "edges.")
    dgl_graph.ndata['l'] = torch.Tensor(mesh.vertices)

    # for i in range(len(mesh.vertices)):
    #     if mesh.vertices[i].all() != dgl_graph.nodes[i].data['l'].numpy()[0].all():
    #         print("{} != {}".format(mesh.vertices[i], dgl_graph.nodes[i].data['l'][0].numpy()))
    
    if save:
        out_path = save_path(path, ".dgl")
        save_file(out_path, dgl_graph)
    return dgl_graph


def dgl2mesh(path, save=False, show = False):
    print("DGL to Mesh")
    in_file = open(path, "rb")
    graph = pickle.load(in_file)
    g = graph.to_networkx(node_attrs='l').to_directed()

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
        for i in range(len(neighbor_list)):
            n1 = neighbor_list[i]
            if traversed[n1] or n1 == crt_node:
                continue
            q.put(n1)
            # for j in range(len(neighbor_list)):
            #     n2 = neighbor_list[j]
            #     if g.has_edge(n1, n2) and n2 != crt_node and n1 != n2:
            #         faces.append([crt_node, n1, n2])

            for j in range(len(neighbor_list)):
                n2 = neighbor_list[j]
                if g.has_edge(n1, n2) and n2 != crt_node and n1 != n2:
                    faces.append([crt_node, n1, n2])

        traversed[crt_node] = True
        count += 1
    mesh.faces = np.array(faces)

    print("Mesh has {} faces".format(len(mesh.faces)))
    print("Mesh has {} edges".format(len(mesh.edges)))

    in_file.close()
    if show:
        mesh.show()
    print("end")
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
    ifshow =False
    path = "./cube.obj"
    graph = mesh2dgl(path, save=True, show = ifshow)

    graph_path = "./cube.dgl"
    mesh = dgl2mesh(graph_path, show = ifshow)

    print(mesh.vertices)
    print(mesh.faces)