from itertools import combinations
from networkx.classes import neighbors
from productions.production import Production


class ProductionP11(Production):
    """
    Production P11 (zmodyfikowana):
    Dzieli sześciokąt z 2 sąsiadującymi węzłami wiszącymi (h=1) na 6 mniejszych czworokątów.
    """

    @property
    def check(self):
        """
        Sprawdza, czy produkcja może zostać zastosowana do wybranego sześciokąta,
        który posiada dokładnie 2 wiszące węzły h=1 na sąsiadujących krawędziach.
        """
        for node, data in self.graph.nodes(data=True):

            if data.get("label") == "P" and data.get("R") == 1:
                neighbors_nodes = list(self.graph.neighbors(node))
                print(neighbors_nodes)
                print([(n, self.graph.nodes[n].get("h")) for n in neighbors_nodes])
                hanging_nodes = [n for n in neighbors_nodes if self.graph.nodes[n].get("h") == 1]
                print(len(hanging_nodes))
                if len(hanging_nodes) == 2:
                    print(self.graph.has_edge(hanging_nodes[0], hanging_nodes[1]))
                    if self.graph.has_edge(hanging_nodes[0], hanging_nodes[1]):

                        non_hanging_nodes = [n for n in neighbors_nodes if self.graph.nodes[n].get("h") == 0]

                        if len(non_hanging_nodes) == 5:

                            neighbors_edges_cnt = 0
                            for n1, n2 in combinations(neighbors_nodes, 2):
                                if self.graph.has_edge(n1, n2):
                                    neighbors_edges_cnt += 1
                            print(neighbors_edges_cnt)
                            if neighbors_edges_cnt == 7:
                                print("prod 11 can be applied to this graph with 2 adjacent hanging nodes")
                                return self._extract_subgraph(node, neighbors_nodes)

        print("prod 11 can't be applied to this graph")
        return None

    def apply(self):
        """Zastosowanie produkcji P11 dla przypadku dwóch wiszących sąsiadujących węzłów."""
        result = self.check

        if not result:
            return

        q_node, nodes = result
        self.subgraph.remove_node(q_node)
        self.graph.remove_node(q_node)

        midpoints = {}
        for (n1, n2) in combinations(nodes, 2):

            if self.subgraph.get_edge_data(n1, n2):
                self._create_midpoint(midpoints, n1, n2)

            elif self.subgraph.degree(n1) == 1 and self.subgraph.degree(n2) == 1:
                self.subgraph.add_edge(n1, n2, label='E', B=1)
                self.graph.add_edge(n1, n2)
                _ = self._create_midpoint(midpoints, n1, n2)

        self._fill_graph(nodes, midpoints)

        self.graph.update(self.subgraph)
