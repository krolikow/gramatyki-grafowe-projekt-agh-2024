from fake_graphs import *
from plot_graph import plot_graph
from productions.p22.production22 import ProductionP22


def graph_missing_vertex() -> nx.Graph:
    G = nx.Graph()
    # Add the center node
    G.add_nodes_from([
        ('v:0.0:0.0', {'label': 'v', 'x': 0.0, 'y': 0.0, 'h': 0}),
        ('v:1.0:0.0', {'label': 'v', 'x': 1.0, 'y': 0.0, 'h': 0}),
        ('v:0.0:1.0', {'label': 'v', 'x': 0.0, 'y': 1.0, 'h': 0}),
        ('v:0.0:0.5', {'label': 'v', 'x': 0.0, 'y': 0.5, 'h': 0}),
        ('v:0.5:0.0', {'label': 'v', 'x': 0.5, 'y': 0.0, 'h': 0}),

        ('v:1.0:0.5', {'label': 'v', 'x': 1.0, 'y': 0.5, 'h': 1}),

        ('v:2.0:0.5', {'label': 'v', 'x': 2.0, 'y': 0.5, 'h': 0}),
        ('v:2.0:1.0', {'label': 'v', 'x': 2.0, 'y': 1.0, 'h': 0}),

        ('P:0.5:0.5', {'label': 'P', 'R': 0}),
        ('Q:1.5:0.75', {'label': 'Q', 'R': 1}),
    ])

    G.add_edges_from([

        ('v:1.0:0.0', 'v:1.0:0.5', {'label': 'E', 'B': 1}),

        ('P:0.5:0.5', 'v:0.0:0.0'),
        ('P:0.5:0.5', 'v:1.0:0.0'),
        ('P:0.5:0.5', 'v:0.0:1.0'),
        ('P:0.5:0.5', 'v:0.0:0.5'),
        ('P:0.5:0.5', 'v:0.5:0.0'),

        ('Q:1.5:0.75', 'v:1.0:0.5'),
        ('Q:1.5:0.75', 'v:2.0:0.5'),
        ('Q:1.5:0.75', 'v:2.0:1.0'),
    ])
    return G


def test():
    graph = graph_missing_vertex()
    production = ProductionP22(graph)
    plot_graph(graph)

    result = production.extract_left_side()
    assert result is None, "No suitable nodes found to apply the production"
