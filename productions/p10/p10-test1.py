import pytest
import networkx as nx

from pytest import FixtureRequest

from productions.p10.production10 import ProductionP10


@pytest.fixture(scope='function')
def prepare_graph_without_hanging(request: type[FixtureRequest]):
    G = nx.Graph()
    G.add_node("S:5.0:5.0", label="S", R=1)
    G.add_nodes_from(
        [
            ("v:0.0:0.0", {"label": "v", "x": 0.0, "y": 0.0, "h": 0}),
            ("v:10.0:0.0", {"label": "v", "x": 10.0, "y": 0.0, "h": 0}),
            ("v:10.0:10.0", {"label": "v", "x": 10.0, "y": 10.0, "h": 0}),
            ("v:0.0:10.0", {"label": "v", "x": 0.0, "y": 10.0, "h": 0}),
            ("v:15.0:5.0", {"label": "v", "x": 15.0, "y": 5.0, "h": 0}),
            ("v:15.0:15.0", {"label": "v", "x": 15.0, "y": 15.0, "h": 0}),
        ]
    )
    G.add_edges_from(
        [
            ("v:0.0:0.0", "v:10.0:0.0", {"label": "E", "B": 1}),
            ("v:15.0:5.0", "v:10.0:10.0", {"label": "E", "B": 1}),
            ("v:10.0:0.0", "v:15.0:5.0", {"label": "E", "B": 1}),
            ("v:10.0:10.0", "v:0.0:10.0", {"label": "E", "B": 1}),
            ("v:0.0:10.0", "v:15.0:15.0", {"label": "E", "B": 1}),
            ("v:15.0:15.0", "v:0.0:0.0", {"label": "E", "B": 1}),

            ("S:5.0:5.0", "v:0.0:0.0"),
            ("S:5.0:5.0", "v:15.0:5.0"),
            ("S:5.0:5.0", "v:10.0:0.0"),
            ("S:5.0:5.0", "v:10.0:10.0"),
            ("S:5.0:5.0", "v:0.0:10.0"),
            ("S:5.0:5.0", "v:15.0:15.0"),

        ]
    )

    return G


@pytest.fixture(scope='function')
def prepare_graph_hanging(request: type[FixtureRequest]):
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

    yield G


def test_positive_p10_check_without_hanging_node(prepare_graph_without_hanging: nx.Graph):
    """check is not None if the graph is valid"""
    assert ProductionP10(prepare_graph_without_hanging).check is None


def test_positive_p10_check(prepare_graph_hanging: nx.Graph):
    """check is not None if the graph is valid"""
    assert ProductionP10(prepare_graph_hanging).check is not None
