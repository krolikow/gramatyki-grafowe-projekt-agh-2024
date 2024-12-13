from fake_graphs import *
from plot_graph import plot_graph
from productions.p11.production11 import ProductionP11
import networkx as nx

if __name__ == '__main__':
    G = nx.Graph()
    G.add_node("S:5.0:5.0", label="S", R=1)

    # Węzły wierzchołkowe sześciokąta z h=0
    G.add_nodes_from(
        [
            ("v:0.0:0.0",   {"label": "v", "x": 0.0,   "y": 0.0,   "h": 0}),
            ("v:10.0:0.0",  {"label": "v", "x": 10.0,  "y": 0.0,   "h": 0}),
            ("v:15.0:5.0",  {"label": "v", "x": 15.0,  "y": 5.0,   "h": 0}),
            ("v:10.0:10.0", {"label": "v", "x": 10.0,  "y": 10.0,  "h": 0}),
            ("v:0.0:10.0",  {"label": "v", "x": 0.0,   "y": 10.0,  "h": 0}),
            ("v:15.0:15.0", {"label": "v", "x": 15.0,  "y": 15.0,  "h": 0}),
        ]
    )

    # Dwa wiszące węzły (h=1) na sąsiednich krawędziach:
    # Pierwszy pomiędzy v:0.0:10.0 a v:7.5:12.5 a następnie v:7.5:12.5 - v:15.0:15.0
    # Drugi pomiędzy v:10.0:10.0 a v:5.0:10.0 a następnie v:5.0:10.0 - v:0.0:10.0
    G.add_node("v:7.5:12.5", label="v", x=7.5, y=12.5, h=1)
    G.add_node("v:5.0:10.0", label="v", x=5.0, y=10.0, h=1)

    G.add_edges_from(
        [
            ("v:0.0:0.0",   "v:10.0:0.0",  {"label": "E", "B": 1}),
            ("v:10.0:0.0",  "v:15.0:5.0",  {"label": "E", "B": 1}),
            ("v:15.0:5.0",  "v:10.0:10.0", {"label": "E", "B": 1}),
            
            # Druga krawędź z wiszącym węzłem:
            ("v:10.0:10.0", "v:5.0:10.0",  {"label": "E", "B": 1}),
            ("v:5.0:10.0",  "v:0.0:10.0",  {"label": "E", "B": 1}),

            # Pierwsza krawędź z wiszącym węzłem:
            ("v:0.0:10.0",  "v:7.5:12.5",  {"label": "E", "B": 1}),
            ("v:7.5:12.5",  "v:15.0:15.0", {"label": "E", "B": 1}),
            
            ("v:15.0:15.0", "v:0.0:0.0",   {"label": "E", "B": 1}),

            # Połączenia do węzła centralnego S
            ("S:5.0:5.0",   "v:0.0:0.0"),
            ("S:5.0:5.0",   "v:10.0:0.0"),
            ("S:5.0:5.0",   "v:15.0:5.0"),
            ("S:5.0:5.0",   "v:10.0:10.0"),
            ("S:5.0:5.0",   "v:0.0:10.0"),
            ("S:5.0:5.0",   "v:15.0:15.0"),
        ]
    )

    plot_graph(G, title="Before Production 11")
    prod11 = ProductionP11(G)
    prod11.apply()
    plot_graph(G, title="After Production 11")
