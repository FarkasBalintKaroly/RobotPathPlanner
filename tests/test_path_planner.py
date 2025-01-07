from src.graph import Graph
from src.path_planner.dijkstra import DijkstraPathPlanner


def test_dijkstra_simple_path():
    """Teszteljük, hogy a Dijkstra működik akadályok nélkül."""
    config = {
        "space_size": [1.0, 1.0, 1.0],
        "grid_resolution": 0.2,
        "obstacles": []
    }
    graph = Graph(config)
    planner = DijkstraPathPlanner(graph)

    start = graph.to_grid_index([0.0, 0.0, 0.0])
    goal = graph.to_grid_index([0.8, 0.8, 0.8])

    # print("Csomópontok:", graph.nodes)
    # print("Szomszédok:", graph.edges)

    assert start in graph.nodes, "Start csomópont nem található a gráfban."
    assert goal in graph.nodes, "Goal csomópont nem található a gráfban."

    path = planner.plan_path(start, goal)

    assert path is not None
    assert path[0] == start
    assert path[-1] == goal


def test_dijkstra_with_obstacles():
    """Teszteljük, hogy a Dijkstra képes elkerülni az akadályokat."""
    config = {
        "space_size": [1.0, 1.0, 1.0],
        "grid_resolution": 0.2,
        "obstacles": [{"start": [0.4, 0.4, 0.4], "end": [0.6, 0.6, 0.6]}]
    }
    graph = Graph(config)
    planner = DijkstraPathPlanner(graph)

    start = (0, 0, 0)
    goal = (4, 4, 4)
    path = planner.plan_path(start, goal)

    assert path is not None
    assert start in path
    assert goal in path
    # Ellenőrizzük, hogy az útvonal elkerüli az akadályt
    obstacle = (2, 2, 2)
    assert obstacle not in path

test_dijkstra_simple_path()