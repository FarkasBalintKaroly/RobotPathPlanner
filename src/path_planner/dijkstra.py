import heapq


class DijkstraPathPlanner:
    def __init__(self, graph):
        """Init Dijkstra Path Planner"""
        self.graph = graph

    def plan_path(self, start, goal):
        """Dijkstra algorithm."""
        if start not in self.graph.nodes or goal not in self.graph.nodes:
            raise ValueError("Start or goal node is not in graph!")

        distances = {node: float('inf') for node in self.graph.nodes}
        distances[start] = 0

        priority_queue = [(0, start)]

        came_from = {}

        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)

            print(f"Current node: {current_node}, Distance: {current_distance}")
            print(f"Neighbors of {current_node}: {self.graph.edges[current_node]}")

            if current_node == goal:
                return self.reconstruct_path(came_from, current_node)

            for neighbor, weight in self.graph.edges[current_node]:
                new_distance = current_distance + weight

                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    came_from[neighbor] = current_node
                    heapq.heappush(priority_queue, (new_distance, neighbor))

        return None


    def reconstruct_path(self, came_from, current):
        """Reconstruct path from goal to start position."""
        path = [current]
        while current in came_from:
            current = came_from[current]
            path.append(current)
        return path[::-1]
