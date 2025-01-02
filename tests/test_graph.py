from src.graph import Graph


def test_graph_creation():
    """Testing the graph creation is good."""
    config = {
        "space_size": [0.4, 0.4, 0.4],
        "grid_resolution": 0.2,
        "obstacles": []
    }

    graph = Graph(config=config)

    # Testing number of nodes
    assert len(graph.nodes) == 8    # 2x2x2 nodes


def test_graph_with_obstacles():
    """Testing the graph if there is obstacle."""
    config = {
        "space_size": [0.4, 0.4, 0.4],
        "grid_resolution": 0.2,
        "obstacles": [{"start": [0.2, 0.2, 0.2], "end": [0.4, 0.4, 0.4]}]
    }

    graph = Graph(config=config)

    assert len(graph.nodes) == 7


test_graph_creation()
test_graph_with_obstacles()