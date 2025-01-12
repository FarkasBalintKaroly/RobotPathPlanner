import heapq


class DijkstraPathPlanner:
    """
    Implements the Dijkstra algorithm for shortest path planning in a graph.

    This class finds the shortest path between a start node and a goal node
    in a given graph using Dijkstra's algorithm.

    Attributes:
        graph (Graph): The graph on which the path planning is performed.
    """
    def __init__(self, graph):
        """
        Initialize the DijkstraPathPlanner with a graph.

        Args:
            graph (Graph): The graph object containing nodes and edges.
        """
        self.graph = graph

    def plan_path(self, start, goal):
        """
        Plan the shortest path from start to goal using Dijkstra's algorithm.

        Args:
            start (tuple): The starting node's coordinates (x, y, z).
            goal (tuple): The goal node's coordinates (x, y, z).

        Returns:
            list: The shortest path as a list of nodes from start to goal.
            None: If no path exists between the start and goal nodes.

        Raises:
            ValueError: If the start or goal node is not in the graph.

        Algorithm:
            - Initialize distances for all nodes as infinity, except the start node (distance 0).
            - Use a priority queue to explore the graph in order of increasing distance.
            - Update distances and track the path to each node using a `came_from` dictionary.
            - Stop when the goal node is reached, and reconstruct the path.
        """
        if start not in self.graph.nodes or goal not in self.graph.nodes:
            raise ValueError("Start or goal node is not in graph!")

        distances = {node: float('inf') for node in self.graph.nodes}
        distances[start] = 0

        priority_queue = [(0, start)]

        came_from = {}

        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)

            if current_node == goal:
                return self.reconstruct_path(came_from, current_node)

            for neighbor, weight in self.graph.edges[current_node]:
                new_distance = current_distance + weight

                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    came_from[neighbor] = current_node
                    heapq.heappush(priority_queue, (new_distance, neighbor))

        return None

    @staticmethod
    def reconstruct_path(came_from, current):
        """
        Reconstruct the path from the goal node to the start node.

        Args:
            came_from (dict): A dictionary mapping each node to its predecessor.
            current (tuple): The goal node coordinates.

        Returns:
            list: The reconstructed path as a list of nodes from start to goal.
        """
        path = [current]
        while current in came_from:
            current = came_from[current]
            path.append(current)
        return path[::-1]
