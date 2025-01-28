from itertools import combinations

from productions.production import Production


def is_valid_middle(graph, a, middle, b) -> bool:
    if not (middle is not None and graph.nodes[middle].get("h") == 1):  # is not hanging middle node
        return False

    data1 = graph.get_edge_data(a, middle)
    data2 = graph.get_edge_data(b, middle)

    return data1["B"] == data2["B"]


def find_middle(graph, n1, n2) -> None | str:
    for n in graph.neighbors(n1):
        if (n in graph.neighbors(n2) and not graph.nodes[n].get("label") == "P"  # is hyperedge
                and graph.nodes[n].get("h") == 1):
            return n
    return None


def is_valid_neighbors(graph, neighbors) -> bool:
    return all(graph.nodes[n].get("h") == 0 for n in neighbors) and len(
        neighbors) == 6  # no node is hanging and there is 6 neighbours


class ProductionP11(Production):
    def extract_left_side(self) -> None | tuple:
        for node, data in self.graph.nodes(data=True):
            if not data.get("label") == "P" or not data.get("R") == 1:  # is not splittable hyperedge
                continue

            neighbors = list(self.graph.neighbors(node))
            if not is_valid_neighbors(self.graph, neighbors):
                continue

            vertex_with_two_hanging_middles = (
                self._find_vertex_with_two_hanging_middles(neighbors)
            )
            if not vertex_with_two_hanging_middles:
                continue

            n1, m12, n2, m13, n3 = vertex_with_two_hanging_middles
            if is_valid_middle(self.graph, n1, m12, n2) and is_valid_middle(self.graph, n1, m13, n3):
                return (
                    self._extract_subgraph(node, neighbors + [m12, m13]),
                    vertex_with_two_hanging_middles,
                )
        return None

    def apply(self):
        result = self.extract_left_side()
        if result is not None:
            (q, neighbors), (n1, m12, n2, m13, n3) = result
            self._remove_nodes(q, neighbors, m12, m13)

            midpoints = {m12: (n1, n2), m13: (n1, n3)}
            self._create_midpoints(neighbors, midpoints)

            phantom_edge_data = {
                (n1, n2): self.graph.get_edge_data(n1, m12),
                (n1, n3): self.graph.get_edge_data(n1, m13),
            }
            self._fill_graph(neighbors, midpoints, edge_data=phantom_edge_data)
            self._update_subgraph_nodes(m12, m13)

            self.graph.update(self.subgraph)



    def _remove_nodes(self, q, neighbors, m12, m13):
        neighbors.remove(m12)
        neighbors.remove(m13)
        self.subgraph.remove_node(q)
        self.graph.remove_node(q)

    def _create_midpoints(self, neighbors, midpoints):
        for a, b in combinations(neighbors, 2):
            if self.subgraph.has_edge(a, b):
                self._create_midpoint(midpoints, a, b)

    def _update_subgraph_nodes(self, m12, m13):
        self.subgraph.nodes[m12]["h"] = 0
        self.subgraph.nodes[m13]["h"] = 0

    def _find_vertex_with_two_hanging_middles(self, neighbors) -> None | list:
        for node in neighbors:
            other_neighbors = [n for n in neighbors if n != node]
            for a, b in combinations(other_neighbors, 2):
                m1 = find_middle(self.graph, node, a)
                m2 = find_middle(self.graph, node, b)
                if m1 and m2:
                    return node, m1, a, m2, b
        return None
