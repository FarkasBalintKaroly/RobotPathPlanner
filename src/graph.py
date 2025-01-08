import math
import numpy as np
from collections import defaultdict


class Graph:
    def __init__(self, config):
        self.space_size = config['space_size']
        self.grid_resolution = config['grid_resolution']
        self.obstacles = config['obstacles']
        # self.start_point = tuple(config['start_point'])
        # self.goal_point = tuple(config['goal_point'])

        self.nodes = set()
        self.edges = defaultdict(list)

        self._create_grid()
        self._remove_obstacle_nodes()
        self._connect_nodes()

    def _create_grid(self):
        """Create grid nodes in 3D space."""
        x_range = np.arange(0, self.space_size[0] + self.grid_resolution, self.grid_resolution)
        y_range = np.arange(0, self.space_size[1] + self.grid_resolution, self.grid_resolution)
        z_range = np.arange(0, self.space_size[2] + self.grid_resolution, self.grid_resolution)

        for x in x_range:
            for y in y_range:
                for z in z_range:
                    self.nodes.add((round(x, 5), round(y, 5), round(z, 5)))

    def _remove_obstacle_nodes(self):
        """Remove nodes that fall within obstacles."""
        def is_in_obstacle(node_, obstacle_):
            return all(obstacle_['start'][i] <= node_[i] <= obstacle_['end'][i] for i in range(3))

        nodes_to_remove = set()
        for node in self.nodes:
            for obstacle in self.obstacles:
                if is_in_obstacle(node, obstacle):
                    nodes_to_remove.add(node)

        self.nodes -= nodes_to_remove

    def _connect_nodes(self):
        """Connect neighboring nodes."""
        for node in self.nodes:
            neighbors = self._get_neighbors(node)
            for neighbor in neighbors:
                if neighbor in self.nodes:
                    weight = self._calculate_distance(node, neighbor)
                    self.edges[node].append((neighbor, weight))

    @staticmethod
    def _calculate_distance(node1, node2):
        """Calculate Euclidean distance between two nodes."""
        return round(math.sqrt(
            (node1[0] - node2[0])**2 +
            (node1[1] - node2[1])**2 +
            (node1[2] - node2[2])**2
        ))

    def _get_neighbors(self, node):
        """Get all potential neighbors of a node in 3D space."""
        directions = [
            (dx, dy, dz)
            for dx in [-self.grid_resolution, 0, self.grid_resolution]
            for dy in [-self.grid_resolution, 0, self.grid_resolution]
            for dz in [-self.grid_resolution, 0, self.grid_resolution]
            if (dx, dy, dz) != (0, 0, 0)
        ]

        neighbors = []
        for dx, dy, dz in directions:
            neighbor = (
                round(node[0] + dx, 5),
                round(node[1] + dy, 5),
                round(node[2] + dz, 5)
            )
            neighbors.append(neighbor)
        return neighbors

    @staticmethod
    def _is_adjacent(node, neighbor):
        """Check if two nodes are adjacent (not diagonal)."""
        diff = [abs(node[i] - neighbor[i]) for i in range(3)]
        return diff.count(0) == 2

    def print_graph(self):
        """Print the graph structure."""
        for node, connections in self.edges.items():
            print(f"Node {node}: {connections}")
