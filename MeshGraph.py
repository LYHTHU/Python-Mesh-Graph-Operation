import dgl


class MeshGraph:
    def __init__(self, graph, faces):
        self.graph = graph
        self.faces = faces
