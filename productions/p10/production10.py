from itertools import combinations

from networkx.classes import neighbors

from productions.production import Production


class ProductionP10(Production):
    """
    Production P10:
    Divides a hexagon with 1 hanging node into 6 smaller hexagons.
    """

    @property
    def check(self):
        """Check if the production can be applied to the selected hexagon with a hanging node."""
        for node, data in self.graph.nodes(data=True):
            if data.get("label") == "S" and data.get("R") == 1:
                neighbors = list(self.graph.neighbors(node))
                if all(self.graph.nodes[n].get("h") == 0 for n in neighbors):
                    neighbors_edges_cnt = 0
                    for n1, n2 in combinations(neighbors, 2):
                        if self.graph.has_edge(n1, n2):
                            neighbors_edges_cnt += 1
                    print(neighbors_edges_cnt)

                    # check if only 2 neighbors have another 1 neighbor with h=1
                    hanging_neighbors_count = 0
                    for neighbor in neighbors:
                        hanging_neighbors = [n for n in self.graph.neighbors(neighbor) if
                                             self.graph.nodes[n].get("h") == 1]
                        if len(hanging_neighbors) == 1:
                            hanging_neighbors_count += 1

                    if neighbors_edges_cnt == 5 and hanging_neighbors_count == 2:
                        print("prod 10 can be applied to this graph")
                        return self._extract_subgraph(node, neighbors)
        print("prod 10 can't be applied to this graph")
        return None

    def apply(self):
        """Apply P10 to divide the hexagon."""
        result = self.check

        if not result:
            return

        q_node, nodes = result
        self.subgraph.remove_node(q_node)
        self.graph.remove_node(q_node)

        midpoints = {}
        for (n1, n2) in combinations(nodes, 2):
            # existing edges
            if self.subgraph.get_edge_data(n1, n2):
                self._create_midpoint(midpoints, n1, n2)
            # artificially add edge to hanging node
            elif self.subgraph.degree(n1) == 1 and self.subgraph.degree(n2) == 1:
                self.subgraph.add_edge(n1, n2, label='E', B=1)
                self.graph.add_edge(n1, n2)
                _ = self._create_midpoint(midpoints, n1, n2)

        self._fill_graph(nodes, midpoints)

        # Replace subgraph in graph
        self.graph.update(self.subgraph)


"""
from fake_graphs import *
from plot_graph import plot_graph
from productions.p10.production10 import ProductionP10

if __name__ == '__main__':
    G = nx.Graph()
    G.add_node("S:5.0:5.0", label="S", R=1)
    G.add_nodes_from(
        [
            ("v:0.0:0.0", {"label": "v", "x": 0.0, "y": 0.0, "h": 0}),
            ("v:10.0:0.0", {"label": "v", "x": 10.0, "y": 0.0, "h": 0}),
            ("v:10.0:10.0", {"label": "v", "x": 10.0, "y": 10.0, "h": 0}),
            ("v:15.0:5.0", {"label": "v", "x": 15.0, "y": 5.0, "h": 0}),
            ("v:7.5:12.5", {"label": "v", "x": 7.5, "y": 12.5, "h": 1}),
            ("v:0.0:10.0", {"label": "v", "x": 0.0, "y": 10.0, "h": 0}),
            ("v:15.0:15.0", {"label": "v", "x": 15.0, "y": 15.0, "h": 0}),
        ]
    )
    G.add_edges_from(
        [
            ("v:0.0:0.0", "v:10.0:0.0", {"label": "E", "B": 1}),
            ("v:15.0:5.0", "v:10.0:10.0", {"label": "E", "B": 1}),
            ("v:10.0:0.0", "v:15.0:5.0", {"label": "E", "B": 1}),
            ("v:10.0:10.0", "v:0.0:10.0", {"label": "E", "B": 1}),
            ("v:0.0:10.0", "v:7.5:12.5", {"label": "E", "B": 1}),
            ("v:7.5:12.5", "v:15.0:15.0", {"label": "E", "B": 1}),
            ("v:15.0:15.0", "v:0.0:0.0", {"label": "E", "B": 1}),

            ("S:5.0:5.0", "v:0.0:0.0"),
            ("S:5.0:5.0", "v:15.0:5.0"),
            ("S:5.0:5.0", "v:10.0:0.0"),
            ("S:5.0:5.0", "v:10.0:10.0"),
            ("S:5.0:5.0", "v:0.0:10.0"),
            ("S:5.0:5.0", "v:15.0:15.0"),

        ]
    )

    plot_graph(G)
    prod10 = ProductionP10(G)
    prod10.apply()
    plot_graph(G)
"""


