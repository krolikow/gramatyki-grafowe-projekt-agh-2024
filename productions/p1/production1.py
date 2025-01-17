from itertools import combinations

from productions.production import Production

class ProductionP1(Production):

    def extract_left_side(self):
        for node, data in self.graph.nodes(data=True):
            if is_hyperedge_node(data) and can_be_splitted(data):
                neighbors = list(self.graph.neighbors(node))
                if all_are_not_hanging_node(self.graph, neighbors) and len(neighbors) == 4:
                    edges = 0
                    for (n1, n2) in combinations(neighbors, 2):
                        if self.graph.has_edge(n1, n2):
                            edges += 1
                    if edges == 4:
                        return self._extract_subgraph(node, neighbors)
        return None

    def apply(self):
        left_side = self.extract_left_side()
        if left_side:
            q, neighbors = left_side
            self.subgraph.remove_node(q)
            self.graph.remove_node(q)

            midpoints = {}
            for (n1, n2) in combinations(neighbors, 2):
                if self.subgraph.has_edge(n1, n2):
                    self._create_midpoint(midpoints, n1, n2)

            self._fill_graph(neighbors, midpoints)

            self.graph.update(self.subgraph)


def is_hyperedge_node(data):
    return data.get('label') == 'Q'


def can_be_splitted(data):
    return data.get('R') == 1


def all_are_not_hanging_node(graph, neighbors):
    return all(graph.nodes[n].get('h') == 0 for n in neighbors)
