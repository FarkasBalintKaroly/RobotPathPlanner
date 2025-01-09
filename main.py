from src.config_loader import ConfigLoader
from src.graph import Graph
from src.path_planner.dijkstra import DijkstraPathPlanner
from src.visualizer import Visualizer3D

# Load config file
config_loader = ConfigLoader()
config = config_loader.load_config(file_path="config/default_config.json")

# Creating graph from config
print("Creating Graph...")
graph = Graph(config=config)
print("Graph created!")

# Planning path with Dijkstra algorithm
print("Planning path...")
path_planner = DijkstraPathPlanner(graph=graph)
start = tuple(config["start_point"])
goal = tuple(config["goal_point"])
path = path_planner.plan_path(start=start, goal=goal)
print("Path planned!")

# Visualizing path and obstacles
print("Visualizing...")
visualizer = Visualizer3D(graph=graph, path=path)
visualizer.plot()
print("Done!")
