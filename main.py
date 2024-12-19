from fake_graphs import *
from plot_graph import plot_graph
from productions.p12.production12 import ProductionP12

if __name__ == '__main__':
    G = nx.Graph()
    # Add the center node
# Add the center node
    G.add_node("S:5.0:5.0", label="P", R=1)

    # Add nodes to form a hexagon with two hanging nodes
    G.add_nodes_from([
        ("v:0.0:5.0", {"label": "v", "x": 0.0, "y": 5.0, "h": 0}),   # Left vertex
        ("v:2.5:8.66", {"label": "v", "x": 2.5, "y": 8.66, "h": 0}),  # Top-left vertex
        ("v:7.5:8.66", {"label": "v", "x": 7.5, "y": 8.66, "h": 0}),  # Top-right vertex
        ("v:10.0:5.0", {"label": "v", "x": 10.0, "y": 5.0, "h": 0}),  # Right vertex
        ("v:7.5:1.34", {"label": "v", "x": 7.5, "y": 1.34, "h": 0}),  # Bottom-right vertex
        ("v:2.5:1.34", {"label": "v", "x": 2.5, "y": 1.34, "h": 0}),  # Bottom-left vertex

        # Hanging nodes (on edges)
        ("v:5.0:8.66", {"label": "v", "x": 5.0, "y": 8.66, "h": 1}),  # Hanging node on top edge
        ("v:5.0:1.34", {"label": "v", "x": 5.0, "y": 1.34, "h": 1}),  # Hanging node on bottom edge
    ])

    # Add edges to form the hexagon and connections to hanging nodes
    G.add_edges_from([
        ("v:0.0:5.0", "v:2.5:8.66", {"label": "E", "B": 1}),
        ("v:7.5:8.66", "v:10.0:5.0", {"label": "E", "B": 1}),
        ("v:10.0:5.0", "v:7.5:1.34", {"label": "E", "B": 1}),
        ("v:2.5:1.34", "v:0.0:5.0", {"label": "E", "B": 1}),

        # Hanging node connections
        ("v:2.5:8.66", "v:5.0:8.66", {"label": "E", "B": 1}),
        ("v:7.5:8.66", "v:5.0:8.66", {"label": "E", "B": 1}),
        ("v:7.5:1.34", "v:5.0:1.34", {"label": "E", "B": 1}),
        ("v:2.5:1.34", "v:5.0:1.34", {"label": "E", "B": 1}),

        # Connections to center node
        ("S:5.0:5.0", "v:0.0:5.0"),
        ("S:5.0:5.0", "v:2.5:8.66"),
        ("S:5.0:5.0", "v:7.5:8.66"),
        ("S:5.0:5.0", "v:10.0:5.0"),
        ("S:5.0:5.0", "v:7.5:1.34"),
        ("S:5.0:5.0", "v:2.5:1.34"),
    ])
    plot_graph(G)
    prod10 = ProductionP12(G)
    prod10.apply()
    plot_graph(G)