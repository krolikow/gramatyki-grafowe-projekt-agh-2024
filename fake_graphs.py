import networkx as nx
from productions.utils import add_hyperedge_to_graph

def valid_graph() -> nx.Graph:
    """4-nodes and one Q-node"""
    G = nx.Graph()
    G.add_node(
        'Q',
        label='Q',
        R=1,
    )
    G.add_nodes_from([
        ('v:0.0:0.0', {'label': 'v', 'x': 0.0, 'y': 0.0, 'h': 0}),
        ('v:1.0:0.0', {'label': 'v', 'x': 1.0, 'y': 0.0, 'h': 0}),
        ('v:1.0:1.0', {'label': 'v', 'x': 1.0, 'y': 1.0, 'h': 0}),
        ('v:0.0:1.0', {'label': 'v', 'x': 0.0, 'y': 1.0, 'h': 0})
    ])
    G.add_edges_from([
        ('v:0.0:0.0', 'v:1.0:0.0', {'label': 'E', 'B': 1}),
        ('v:1.0:0.0', 'v:1.0:1.0', {'label': 'E', 'B': 1}),
        ('v:1.0:1.0', 'v:0.0:1.0', {'label': 'E', 'B': 1}),
        ('v:0.0:1.0', 'v:0.0:0.0', {'label': 'E', 'B': 1}),
        ('Q', 'v:0.0:0.0'),
        ('Q', 'v:1.0:0.0'),
        ('Q', 'v:1.0:1.0'),
        ('Q', 'v:0.0:1.0'),
    ])

    return G

def valid_graph2() -> nx.Graph:
    """5-nodes and one Q-node"""
    G = nx.Graph()
    G.add_node(
        'Q',
        label='Q',
        R=1,
    )
    G.add_nodes_from([
        ('v:0.0:0.0', {'label': 'v', 'x': 0.0, 'y': 0.0, 'h': 0}),
        ('v:1.0:0.0', {'label': 'v', 'x': 1.0, 'y': 0.0, 'h': 0}),
        ('v:1.0:1.0', {'label': 'v', 'x': 1.0, 'y': 1.0, 'h': 0}),
        ('v:0.0:1.0', {'label': 'v', 'x': 0.0, 'y': 1.0, 'h': 0}),
        ('v:1.0:0.5', {'label': 'v', 'x': 1.0, 'y': 0.5, 'h': 1}),
    ])
    G.add_edges_from([
        ('v:0.0:0.0', 'v:1.0:0.0', {'label': 'E', 'B': 1}),
        ('v:1.0:0.0', 'v:1.0:0.5', {'label': 'E', 'B': 1}),
        ('v:1.0:0.5', 'v:1.0:1.0', {'label': 'E', 'B': 1}),
        ('v:1.0:1.0', 'v:0.0:1.0', {'label': 'E', 'B': 1}),
        ('v:0.0:1.0', 'v:0.0:0.0', {'label': 'E', 'B': 1}),
        ('Q', 'v:0.0:0.0'),
        ('Q', 'v:1.0:0.0'),
        ('Q', 'v:1.0:1.0'),
        ('Q', 'v:0.0:1.0'),
    ])

    return G

def start_graph() -> nx.Graph:
    G = nx.Graph()

    nodes = [
        ('v:0:0', {'label': 'v', 'x': 0, 'y': 0, 'h': 0}),
        ('v:16:0', {'label': 'v', 'x': 16, 'y': 0, 'h': 0}),
        ('v:0:16', {'label': 'v', 'x': 0, 'y': 16, 'h': 0}),
        ('v:16:16', {'label': 'v', 'x': 16, 'y': 16, 'h': 0}),
        ('v:2:8', {'label': 'v', 'x': 2, 'y': 8, 'h': 0}),
        ('v:5:3', {'label': 'v', 'x': 5, 'y': 3, 'h': 0}),
        ('v:5:13', {'label': 'v', 'x': 5, 'y': 13, 'h': 0}),
        ('v:11:3', {'label': 'v', 'x': 11, 'y': 3, 'h': 0}),
        ('v:11:13', {'label': 'v', 'x': 11, 'y': 13, 'h': 0}),
        ('v:14:8', {'label': 'v', 'x': 14, 'y': 8, 'h': 0}),
        ('v:0:8', {'label': 'v', 'x': 0, 'y': 8, 'h': 0}),
        ('v:16:8', {'label': 'v', 'x': 16, 'y': 8, 'h': 0}),
    ]

    edges = [
        ('v:0:0', 'v:16:0', {'label': 'E', 'B': 1}),
        ('v:16:0', 'v:16:16', {'label': 'E', 'B': 1}),
        ('v:16:16', 'v:0:16', {'label': 'E', 'B': 1}),
        ('v:0:16', 'v:0:0', {'label': 'E', 'B': 1}),
        ('v:0:16', 'v:5:13', {'label': 'E', 'B': 0}),
        ('v:0:0', 'v:5:3', {'label': 'E', 'B': 0}),
        ('v:16:16', 'v:11:13', {'label': 'E', 'B': 0}),
        ('v:16:0', 'v:11:3', {'label': 'E', 'B': 0}),
        ('v:5:3', 'v:11:3', {'label': 'E', 'B': 0}),
        ('v:5:13', 'v:11:13', {'label': 'E', 'B': 0}),
        ('v:11:3', 'v:14:8', {'label': 'E', 'B': 0}),
        ('v:11:13', 'v:14:8', {'label': 'E', 'B': 0}),
        ('v:2:8', 'v:5:13', {'label': 'E', 'B': 0}),
        ('v:2:8', 'v:5:3', {'label': 'E', 'B': 0}),
        ('v:0:8', 'v:2:8', {'label': 'E', 'B': 0}),
        ('v:14:8', 'v:16:8', {'label': 'E', 'B': 0}),
        ('v:0:0', 'v:0:8', {'label': 'E', 'B': 1}),
        ('v:0:8', 'v:0:16', {'label': 'E', 'B': 1}),
        ('v:16:0', 'v:16:8', {'label': 'E', 'B': 1}),
        ('v:16:16', 'v:16:8', {'label': 'E', 'B': 1}),
    ]

    G.add_nodes_from(nodes)
    G.add_edges_from(edges)
    
    add_hyperedge_to_graph(G, ['v:0:16', 'v:5:13', 'v:2:8', 'v:0:8'], breakable=False, unique_id=True)
    add_hyperedge_to_graph(G, ['v:0:16', 'v:5:13', 'v:11:13', 'v:16:16'], breakable=False, unique_id=True)
    add_hyperedge_to_graph(G, ['v:11:13', 'v:14:8', 'v:16:8', 'v:16:16'], breakable=False, unique_id=True)
    add_hyperedge_to_graph(G, ['v:14:8', 'v:16:8', 'v:16:0', 'v:11:3'], breakable=False, unique_id=True)
    add_hyperedge_to_graph(G, ['v:5:3', 'v:11:3', 'v:16:0', 'v:0:0'], breakable=False, unique_id=True)
    add_hyperedge_to_graph(G, ['v:0:8', 'v:2:8', 'v:5:3', 'v:0:0'], breakable=False, unique_id=True)
    add_hyperedge_to_graph(G, ['v:5:13', 'v:11:13', 'v:14:8', 'v:11:3', 'v:5:3', 'v:2:8'], breakable=False, unique_id=True)

    return G
