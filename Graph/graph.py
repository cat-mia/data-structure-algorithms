class Node:
    def __init__(self, val) -> None:
        self.nexts = []
        self.edges = []
        self.val = val
        self.in_degree = 0
        self.out_degree = 0

class Edge:
    def __init__(self) -> None:
        self.weight = 0
        self.start = None
        self.end = None

class Graph:
    def __init__(self) -> None:
        self.nodes = []
        self.edges = []

    def create_from_matrix(self):
        pass