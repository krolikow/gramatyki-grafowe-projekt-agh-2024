from itertools import combinations

from productions.production import Production


class ProductionP11(Production):
    def extract_left_side(self) -> None | tuple:
        for node, data in self.graph.nodes(data=True):
            if not is_splittable_hyperedge_node(data):
                continue

            neighbors = list(self.graph.neighbors(node))
            if not self._is_valid_neighbors(neighbors):
                continue

            vertex_with_two_hanging_middles = (
                self._find_vertex_with_two_hanging_middles(neighbors)
            )
            if not vertex_with_two_hanging_middles:
                continue

            n1, m12, n2, m13, n3 = vertex_with_two_hanging_middles
            if self._is_valid_middle(n1, m12, n2) and self._is_valid_middle(
                n1, m13, n3
            ):
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

    def _is_valid_neighbors(self, neighbors) -> bool:
        return self._all_are_not_hanging_node(neighbors) and len(neighbors) == 6

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

    def _all_are_not_hanging_node(self, neighbors) -> bool:
        return all(self.graph.nodes[n].get("h") == 0 for n in neighbors)

    def _find_vertex_with_two_hanging_middles(self, neighbors) -> None | list:
        for node in neighbors:
            other_neighbors = [n for n in neighbors if n != node]
            for a, b in combinations(other_neighbors, 2):
                m1 = self._find_middlepoint(node, a)
                m2 = self._find_middlepoint(node, b)
                if m1 and m2:
                    return node, m1, a, m2, b
        return None

    def _find_middlepoint(self, n1, n2) -> None | str:
        for n in self.graph.neighbors(n1):
            if (
                n in self.graph.neighbors(n2)
                and not is_hyperedge_node(self.graph.nodes[n])
                and self.graph.nodes[n].get("h") == 1
            ):
                return n
        return None

    def _is_valid_middle(self, a, middle, b) -> bool:
        if not self._is_hanging_middle(middle):
            return False

        data1 = self.graph.get_edge_data(a, middle)
        data2 = self.graph.get_edge_data(b, middle)

        return data1["B"] == data2["B"]

    def _is_hanging_middle(self, middle) -> bool:
        return middle is not None and self.graph.nodes[middle].get("h") == 1


def is_splittable_hyperedge_node(data) -> bool:
    return is_hyperedge_node(data) and data.get("R") == 1


def is_hyperedge_node(data) -> bool:
    return data.get("label") == "P"