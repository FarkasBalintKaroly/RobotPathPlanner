import numpy as np


class Graph:

    def __init__(self, config):
        self.space_size = config["space_size"]
        self.grid_resolution = config["grid_resolution"]
        self.obstacles = config["obstacles"]
        self.nodes = []
        self.edges = {}

        self.create_graph()

    def create_graph(self):
        """Creating graph."""
        # Creating nodes
        x_range = int(self.space_size[0] / self.grid_resolution)
        y_range = int(self.space_size[1] / self.grid_resolution)
        z_range = int(self.space_size[2] / self.grid_resolution)

        for x in range(x_range):
            for y in range(y_range):
                for z in range(z_range):
                    node = (x, y, z)
                    if not self.is_obstacle(node):
                        print(f"Hozzáadott csomópont: {node}")
                        self.nodes.append(node)
                        self.edges[node] = self.get_neighbors(node)

    def is_obstacle(self, node):
        x, y, z = [coord * self.grid_resolution for coord in node]
        for obstacle in self.obstacles:
            if (
                    obstacle["start"][0] <= x <= obstacle["end"][0]
                    and obstacle["start"][1] <= y <= obstacle["end"][1]
                    and obstacle["start"][2] <= z <= obstacle["end"][2]
            ):
                print(f"Akadály csomópont: {node}")
                return True
        return False

    def get_neighbors(self, node):
        """Lekérdezi egy csomópont szomszédait és azok súlyait."""
        neighbors = []
        directions = [
            (1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1),
            (1, 1, 0), (-1, -1, 0), (1, 0, 1), (-1, 0, -1), (0, 1, 1), (0, -1, -1),
            (1, 1, 1), (-1, -1, -1)
        ]
        for dx, dy, dz in directions:
            neighbor = (node[0] + dx, node[1] + dy, node[2] + dz)
            if neighbor in self.nodes:
                weight = ((dx ** 2 + dy ** 2 + dz ** 2) ** 0.5) * self.grid_resolution
                neighbors.append((neighbor, weight))
        return neighbors

    def to_grid_index(self, coords):
        """Converting coordinates to grid index."""
        return tuple(int(coord / self.grid_resolution) for coord in coords)

