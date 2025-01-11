import unittest

from src.config_loader import ConfigLoader
from src.graph import Graph
from src.path_planner.dijkstra import DijkstraPathPlanner
from src.visualizer import Visualizer3D


class TestConfigLoader(unittest.TestCase):

    def test_valid_config(self):
        config_loader = ConfigLoader()
        config = config_loader.load_config(file_path="../config/default_config.json")
        self.assertIn("space_size", config)
        self.assertIn("grid_resolution", config)
        self.assertIn("obstacles", config)

    def test_invalid_config(self):
        with self.assertRaises(ValueError):
            config_loader = ConfigLoader()
            config_loader.load_config("../config/invalid_config.json")

    def test_missing_file(self):
        with self.assertRaises(FileNotFoundError):
            config_loader = ConfigLoader()
            config_loader.load_config("config/nonexistent_config.json")


class TestGraph(unittest.TestCase):

    def setUp(self):
        config = {
            "space_size": [1.0, 1.0, 1.0],
            "grid_resolution": 0.5,
            "obstacles": [{"start": [0.5, 0.5, 0.5], "end": [1.0, 1.0, 1.0]}]
        }
        self.graph = Graph(config=config)

    def test_obstacle_removal(self):
        self.assertNotIn((0.75, 0.75, 0.75), self.graph.nodes)

    def test_neighbors_connection(self):
        neighbors = self.graph.edges[(0.0, 0.0, 0.0)]
        self.assertTrue(any(n[0] == (0.5, 0.0, 0.0) for n in neighbors))
        self.assertTrue(any(n[0] == (0.0, 0.5, 0.0) for n in neighbors))


class TestDijkstraPathPlanner(unittest.TestCase):

    def setUp(self):
        config = {
            "space_size": [1.0, 1.0, 1.0],
            "grid_resolution": 0.5,
            "obstacles": [{"start": [0.5, 0.5, 0.5], "end": [1.0, 1.0, 1.0]}]
        }
        self.graph = Graph(config)
        self.planner = DijkstraPathPlanner(self.graph)

    def test_simple_path(self):
        path = self.planner.plan_path((0.0, 0.0, 0.0), (0.5, 0.0, 0.0))
        self.assertEqual(path, [(0.0, 0.0, 0.0), (0.5, 0.0, 0.0)])


class TestVisualizer(unittest.TestCase):

    def setUp(self):
        config = {
            "space_size": [1.0, 1.0, 1.0],
            "grid_resolution": 0.5,
            "obstacles": [{"start": [0.5, 0.5, 0.5], "end": [1.0, 1.0, 1.0]}]
        }
        self.graph = Graph(config)
        self.path = [(0.0, 0.0, 0.0), (0.5, 0.0, 0.0), (0.5, 0.5, 0.0)]

    def test_visualizer_3d(self):
        visualizer3d = Visualizer3D(self.graph, self.path)
        try:
            visualizer3d.plot()
        except Exception as e:
            self.fail(f"Visualizer3D.plot() error: {e}")


if __name__ == "__main__":
    unittest.main()
