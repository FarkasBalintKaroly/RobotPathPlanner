from src.graph import Graph
from src.path_planner.dijkstra import DijkstraPathPlanner
from src.visualizer import Visualizer2D, Visualizer3D


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

    path = planner.plan_path(start, goal)

    visualizer2d = Visualizer2D(graph=graph, path=path)
    visualizer2d.plot()

    visualizer3d = Visualizer3D(graph=graph, path=path)
    visualizer3d.plot()


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

    visualizer2d = Visualizer2D(graph=graph, path=path)
    visualizer2d.plot()

    visualizer3d = Visualizer3D(graph=graph, path=path)
    visualizer3d.plot()


# test_dijkstra_simple_path()
# test_dijkstra_with_obstacles()
