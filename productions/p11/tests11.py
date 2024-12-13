import pytest
import networkx as nx

from pytest import FixtureRequest

from productions.p11.production11 import ProductionP11


@pytest.fixture(scope='function')
def prepare_graph_two_hanging(request: type[FixtureRequest]):
    G = nx.Graph()
    # Węzeł centralny z R=1
    G.add_node("S:5.0:5.0", label="S", R=1)

    # Węzły wierzchołkowe sześciokąta z h=0
    # Załóżmy, że tworzą one pewien heksagon jak poprzednio
    G.add_nodes_from(
        [
            ("v:0.0:0.0", {"label": "v", "x": 0.0, "y": 0.0, "h": 0}),
            ("v:10.0:0.0", {"label": "v", "x": 10.0, "y": 0.0, "h": 0}),
            ("v:15.0:5.0", {"label": "v", "x": 15.0, "y": 5.0, "h": 0}),
            ("v:10.0:10.0", {"label": "v", "x": 10.0, "y": 10.0, "h": 0}),
            ("v:0.0:10.0", {"label": "v", "x": 0.0, "y": 10.0, "h": 0}),
            ("v:15.0:15.0", {"label": "v", "x": 15.0, "y": 15.0, "h": 0}),
        ]
    )

    # Dodajemy dwa węzły wiszące (h=1) na dwóch sąsiednich krawędziach
    # Pierwszy wiszący węzeł na krawędzi pomiędzy v:0.0:10.0 a v:15.0:15.0
    G.add_node("v:7.5:12.5", label="v", x=7.5, y=12.5, h=1)

    # Drugi wiszący węzeł na krawędzi pomiędzy v:10.0:10.0 a v:0.0:10.0
    # W ten sposób mamy dwie krawędzie z h=1, które sąsiadują ze sobą w wielokącie
    G.add_node("v:5.0:10.0", label="v", x=5.0, y=10.0, h=1)

    # Krawędzie oryginalnego sześciokąta zostają odpowiednio podzielone:
    # Zamiast ("v:0.0:10.0", "v:15.0:15.0") mamy teraz ("v:0.0:10.0", "v:7.5:12.5") i ("v:7.5:12.5", "v:15.0:15.0")
    # Zamiast ("v:10.0:10.0", "v:0.0:10.0") mamy teraz ("v:10.0:10.0", "v:5.0:10.0") i ("v:5.0:10.0", "v:0.0:10.0")

    G.add_edges_from(
        [
            ("v:0.0:0.0", "v:10.0:0.0", {"label": "E", "B": 1}),
            ("v:10.0:0.0", "v:15.0:5.0", {"label": "E", "B": 1}),
            ("v:15.0:5.0", "v:10.0:10.0", {"label": "E", "B": 1}),

            # Pierwsza krawędź z węzłem wiszącym h=1
            ("v:10.0:10.0", "v:5.0:10.0", {"label": "E", "B": 1}),
            ("v:5.0:10.0", "v:0.0:10.0", {"label": "E", "B": 1}),

            # Druga krawędź z węzłem wiszącym h=1
            ("v:0.0:10.0", "v:7.5:12.5", {"label": "E", "B": 1}),
            ("v:7.5:12.5", "v:15.0:15.0", {"label": "E", "B": 1}),

            ("v:15.0:15.0", "v:0.0:0.0", {"label": "E", "B": 1}),

            # Połączenia centralnego węzła S z wierzchołkami heksagonu
            ("S:5.0:5.0", "v:0.0:0.0"),
            ("S:5.0:5.0", "v:10.0:0.0"),
            ("S:5.0:5.0", "v:15.0:5.0"),
            ("S:5.0:5.0", "v:10.0:10.0"),
            ("S:5.0:5.0", "v:0.0:10.0"),
            ("S:5.0:5.0", "v:15.0:15.0"),
        ]
    )

    yield G


def test_positive_p11_check(prepare_graph_two_hanging: nx.Graph):
    """check is not None if the graph is valid for ProductionP11"""
    assert ProductionP11(prepare_graph_two_hanging).check is not None
