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

        # Zliczenie hanging nodes
        h_cnt = 0
        for node, data in self.graph.nodes(data=True):
            if data.get("h") == 1:
                h_cnt += 1
        
        print(h_cnt)

        # Sprawdzenie, czy hanging nodes sąsdiają ze sobą
        if h_cnt != 2:
            print("prod 11 can't be applied to this graph")
            return False
        hanging_nodes_neighbors = set()
        for node, data in self.graph.nodes(data=True):
            if data.get("h") == 1:
                for neighbor in self.graph.neighbors(node):
                    hanging_nodes_neighbors.add(neighbor)
        if len(hanging_nodes_neighbors) == 3:
            
            return True
        print("prod 11 can't be applied to this graph")
        return False
    

    def apply(self):
        """Apply P10 to divide the hexagon."""
        result = self.check

        if not result:
            return

        q_node, nodes = result
        self.subgraph.remove_node(q_node)
        self.graph.remove_node(q_node)

        h_nodes = {}
        for n, n_attrs in self.graph.nodes.items():
            if n_attrs.get("h") == 1:
                v_neighbors = list(self.graph.neighbors(n))
                if len(v_neighbors) != 2:
                    raise ValueError("Hanging node has more than 2 neighbors")
                n1, n2 = v_neighbors
                b1 = self.graph.get_edge_data(n, n1).get("B")
                b2 = self.graph.get_edge_data(n, n2).get("B")
                if b1 != b2:
                    raise ValueError("Hanging node has different B values")
                h_nodes[n] = {"neighbors": v_neighbors, "B": b1}

        for n in h_nodes.keys():
            self.graph.remove_node(n)

        midpoints = {}
        for (n1, n2) in combinations(nodes, 2):
            if self.subgraph.get_edge_data(n1, n2):
                self._create_midpoint(midpoints, n1, n2)

        for n_attrs in h_nodes.values():
            n1, n2 = n_attrs["neighbors"]
            B = n_attrs["B"]
            self.subgraph.add_edge(n1, n2, label='E', B=B)
            self.graph.add_edge(n1, n2)
            _ = self._create_midpoint(midpoints, n1, n2)

        self._fill_graph(nodes, midpoints)

        # Replace subgraph in graph
        self.graph.update(self.subgraph)