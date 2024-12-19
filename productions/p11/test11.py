import networkx as nx
from production11 import P11  # assuming P11 and the Production base class are defined in production11.py

def build_test_graph_for_p11():
    # Build a graph that matches the LHS pattern of P11
    G = nx.Graph()

    # LHS nodes:
    # Corner nodes: n0, n1, n2, n3, n4
    # Hanging nodes: n5, n6 (with h=True)
    # p-hyperedge: p0
    G.add_node('n0', label='v', x=0,    y=0,    h=False)
    G.add_node('n1', label='v', x=1,    y=0,    h=False)
    G.add_node('n2', label='v', x=1,    y=1,    h=False)
    G.add_node('n3', label='v', x=0,    y=1,    h=False)
    G.add_node('n4', label='v', x=1.83, y=0.5,  h=False)
    G.add_node('n5', label='v', x=0.5,  y=0,    h=True)
    G.add_node('n6', label='v', x=0,    y=0.5,  h=True)
    G.add_node('p0', label='p')  # p-hyperedge

    # Edges forming a cycle: (n0->n5->n1->n4->n2->n3->n6->n0)
    cycle = [('n0','n5'), ('n5','n1'), ('n1','n4'), ('n4','n2'), ('n2','n3'), ('n3','n6'), ('n6','n0')]
    for (a,b) in cycle:
        G.add_edge(a, b, label='E', B=0)

    # p-hyperedge connected to corner nodes (n0,n1,n2,n3,n4)
    for cn in ('n0','n1','n2','n3','n4'):
        G.add_edge('p0', cn, label='H', B=0)

    return G


def test_p11():
    G = build_test_graph_for_p11()
    p11 = P11(G)

    # Check if LHS can be extracted
    mapping = p11.extract_left_side()
    assert mapping is not None, "LHS subgraph for P11 was not found!"

    # Apply the production
    p11.apply()

    # Now we need to define the expected graph structure after applying P11.
    # Run your code and print(nx.to_dict_of_dicts(G)) after p11.apply() to get the actual structure.
    # Then copy and paste that structure here as expected_graph.
    expected_graph = {
        # Fill this dictionary with the actual expected output after P11 is applied.
        # Example:
        # 'v:0.9:0.4': {
        #    'some_other_node': { 'B':0, 'label':'E' },
        #    ...
        # },
        # 'q:...': {...},
        # ...
    }

    # Make sure you have filled expected_graph properly before running the test.

    assert expected_graph, "expected_graph is empty! Please fill it with the correct expected structure."

    actual_graph = nx.to_dict_of_dicts(G)
    assert expected_graph == actual_graph, "The resulting graph after applying P11 does not match the expected structure!"
    print("P11 test passed successfully!")
