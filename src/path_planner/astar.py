import heapq
import math


class AStarPathPlanner:

    def __init__(self, graph):
        self.graph = graph

    @staticmethod
    def heuristic(node, goal):
        """Calculate Euclidean distance for heuristic."""
        return math.sqrt(sum((node[i] - goal[i]) ** 2 for i in range(3)))

    def plan_path(self, start, goal):
        """A* algorithm for optimal path."""
        open_set = []
        heapq.heappush(open_set, (0, start))
        came_from = {}
        g_score = {node: float('inf') for node in self.graph.nodes}
        g_score[start] = 0
        f_score = {node: float('inf') for node in self.graph.nodes}
        f_score[start] = self.heuristic(node=start, goal=goal)

        while open_set:
            _, current = heapq.heappop(open_set)

            if current == goal:
                return self.reconstruct_path(came_from, current)

            for neighbor, weight in self.graph.edges[current]:
                tentative_g_score = g_score[current] + weight
                if tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + self.heuristic(node=neighbor, goal=goal)
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))

        return None

    @staticmethod
    def reconstruct_path(came_from, current):
        """Reconstruct path from goal to start point."""
        path = [current]
        while current in came_from:
            current = came_from[current]
            path.append(current)
        return path[::-1]
