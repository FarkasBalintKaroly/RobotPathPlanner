import math
import numpy as np
from collections import defaultdict


class Graph:
    """
    Represents a 3D grid graph with nodes and edges.

    This class generates a 3D grid based on the given configuration, removes nodes
    that fall within obstacles, and connects nodes to their neighbors.

    Attributes:
        space_size (list): The dimensions of the 3D space [x, y, z].
        grid_resolution (float): The distance between adjacent nodes in the grid.
        obstacles (list): A list of obstacles, each defined by 'start' and 'end' coordinates.
        nodes (set): A set of all valid nodes in the graph.
        edges (dict): A dictionary mapping each node to its connected neighbors and weights.
    """

    def __init__(self, config):
        """
        Initialize the graph with the given configuration.

        Args:
            config (dict): Configuration containing 'space_size', 'grid_resolution', and 'obstacles'.
        """
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
        """
        Create grid nodes in 3D space.

        Generates a grid of nodes within the defined space size and resolution.
        """
        x_range = np.arange(0, self.space_size[0] + self.grid_resolution, self.grid_resolution)
        y_range = np.arange(0, self.space_size[1] + self.grid_resolution, self.grid_resolution)
        z_range = np.arange(0, self.space_size[2] + self.grid_resolution, self.grid_resolution)

        for x in x_range:
            for y in y_range:
                for z in z_range:
                    self.nodes.add((round(x, 5), round(y, 5), round(z, 5)))

    def _remove_obstacle_nodes(self):
        """
        Remove nodes that fall within obstacles.

        Nodes that are within any defined obstacle range will be excluded from the graph.
        """
        def is_in_obstacle(node_, obstacle_):
            return all(obstacle_['start'][i] <= node_[i] <= obstacle_['end'][i] for i in range(3))

        nodes_to_remove = set()
        for node in self.nodes:
            for obstacle in self.obstacles:
                if is_in_obstacle(node, obstacle):
                    nodes_to_remove.add(node)

        self.nodes -= nodes_to_remove

    def _connect_nodes(self):
        """
        Connect neighboring nodes.

        Establish edges between nodes and their neighbors with the calculated weights.
        """
        for node in self.nodes:
            neighbors = self._get_neighbors(node)
            for neighbor in neighbors:
                if neighbor in self.nodes:
                    weight = self._calculate_distance(node, neighbor)
                    self.edges[node].append((neighbor, weight))

    @staticmethod
    def _calculate_distance(node1, node2):
        """
        Calculate the Euclidean distance between two nodes.

        Args:
            node1 (tuple): The first node coordinates (x, y, z).
            node2 (tuple): The second node coordinates (x, y, z).

        Returns:
            float: The Euclidean distance between the two nodes.
        """
        return round(math.sqrt(
            (node1[0] - node2[0])**2 +
            (node1[1] - node2[1])**2 +
            (node1[2] - node2[2])**2
        ), 5)

    def _get_neighbors(self, node):
        """
        Get all potential neighbors of a node in 3D space.

        Args:
            node (tuple): The coordinates of the current node (x, y, z).

        Returns:
            list: A list of potential neighbor nodes.
        """
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
        """
        Check if two nodes are adjacent (not diagonal).

        Args:
            node (tuple): The first node coordinates (x, y, z).
            neighbor (tuple): The second node coordinates (x, y, z).

        Returns:
            bool: True if the nodes are adjacent, False otherwise.
        """
        diff = [abs(node[i] - neighbor[i]) for i in range(3)]
        return diff.count(0) == 2

    def print_graph(self):
        """
        Print the graph structure.

        Prints each node and its connected neighbors with weights.
        """
        for node, connections in self.edges.items():
            print(f"Node {node}: {connections}")

    def export_to_dict(self):
        """
        Export the graph structure to a dictionary.

        Returns:
            dict: A dictionary representation of the graph with nodes and edges.
        """
        return {
            "nodes": list(self.nodes),
            "edges": {str(node): connections for node, connections in self.edges.items()}
        }
