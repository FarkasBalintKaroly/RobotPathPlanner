from src.graph import Graph
from src.path_planner.dijkstra import DijkstraPathPlanner


def test_dijkstra_simple_path():
    """Testing Dijkstra without obstacles."""
    config = {
        "space_size": [1.0, 1.0, 1.0],
        "grid_resolution": 0.2,
        "obstacles": []
    }
    graph = Graph(config)
    planner = DijkstraPathPlanner(graph)

    start = (0, 0, 0)
    goal = (1, 1, 1)

    assert start in graph.nodes, "Start node not found in graph."
    assert goal in graph.nodes, "Goal node not found in graph."

    path = planner.plan_path(start, goal)

    assert path is not None
    assert path[0] == start
    assert path[-1] == goal

    print("Success!")
    print("Path:")
    for node in path:
        print(node)


def test_dijkstra_with_obstacles():
    """Testing Dijkstra with obstacles."""
    config = {
        "space_size": [1.0, 1.0, 1.0],
        "grid_resolution": 0.2,
        "obstacles": [{"start": [0.4, 0.4, 0.4], "end": [0.6, 0.6, 0.6]}]
    }
    graph = Graph(config)
    planner = DijkstraPathPlanner(graph)

    start = (0, 0, 0)
    goal = (1, 1, 1)
    path = planner.plan_path(start, goal)

    assert path is not None
    assert start in path
    assert goal in path

    print("Success!")
    print("Path:")
    for node in path:
        print(node)


# test_dijkstra_simple_path()
# test_dijkstra_with_obstacles()
