import networkx as nx

from plot_graph import plot_graph
from productions.p11.production11 import ProductionP11


def graph_from_p12() -> nx.Graph:
    G = nx.Graph()
    # Add the center node
    G.add_node("S:5.0:5.0", label="P", R=1)
    # Add nodes to form a hexagon with two hanging nodes
    G.add_nodes_from([
        ("v:0.0:5.0", {"label": "v", "x": 0.0, "y": 5.0, "h": 0}),  # Left vertex
        ("v:2.5:8.66", {"label": "v", "x": 2.5, "y": 8.66, "h": 0}),  # Top-left vertex
        ("v:7.5:8.66", {"label": "v", "x": 7.5, "y": 8.66, "h": 0}),  # Top-right vertex
        ("v:10.0:5.0", {"label": "v", "x": 10.0, "y": 5.0, "h": 0}),  # Right vertex
        ("v:7.5:1.34", {"label": "v", "x": 7.5, "y": 1.34, "h": 0}),  # Bottom-right vertex
        ("v:2.5:1.34", {"label": "v", "x": 2.5, "y": 1.34, "h": 0}),  # Bottom-left vertex

        # Hanging nodes (on edges)
        ("v:5.0:8.66", {"label": "v", "x": 5.0, "y": 8.66, "h": 1}),  # Hanging node on top edge
        ("v:8.75:3.17", {"label": "v", "x": 8.75, "y": 3.17, "h": 1}),  # Hanging node on bottom edge
    ])

    # Add edges to form the hexagon and connections to hanging nodes
    G.add_edges_from([
        ("v:2.5:8.66", "v:0.0:5.0", {"label": "E", "B": 1}),
        ("v:7.5:8.66", "v:10.0:5.0", {"label": "E", "B": 1}),
        ("v:7.5:1.34", "v:2.5:1.34", {"label": "E", "B": 1}),
        ("v:2.5:1.34", "v:0.0:5.0", {"label": "E", "B": 1}),

        # Hanging node connections
        ("v:5.0:8.66", "v:7.5:8.66", {"label": "E", "B": 1}),
        ("v:2.5:8.66", "v:5.0:8.66", {"label": "E", "B": 1}),
        ("v:7.5:1.34", "v:8.75:3.17", {"label": "E", "B": 1}),
        ("v:8.75:3.17", "v:10.0:5.0", {"label": "E", "B": 1}),

        # Connections to center node
        ("S:5.0:5.0", "v:0.0:5.0"),
        ("S:5.0:5.0", "v:2.5:8.66"),
        ("S:5.0:5.0", "v:7.5:8.66"),
        ("S:5.0:5.0", "v:10.0:5.0"),
        ("S:5.0:5.0", "v:7.5:1.34"),
        ("S:5.0:5.0", "v:2.5:1.34"),
    ])

    return G


def test():
    graph = graph_from_p12()
    production = ProductionP11(graph)
    plot_graph(graph)
    result = production.extract_left_side()
    assert result is None, "No suitable nodes found to apply the production"
