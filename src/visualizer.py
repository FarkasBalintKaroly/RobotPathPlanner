import matplotlib.pyplot as plt


class Visualizer:
    """
    Base visualizer class for plotting graphs and paths in 2D and 3D.

    Attributes:
        graph (Graph): The graph object containing nodes, edges, and obstacles.
        path (list): The planned path as a list of nodes.
    """

    def __init__(self, graph, path):
        """
        Initialize the Visualizer with a graph and path.

        Args:
            graph (Graph): The graph object.
            path (list): The planned path as a list of nodes.
        """
        self.graph = graph
        self.path = path

    def _plot_obstacles_2d(self, ax, plane):
        """
        Plot obstacles in 2D for the given plane.

        Args:
            ax (matplotlib.axes.Axes): The Matplotlib axis object.
            plane (tuple): The plane to plot ('x', 'y') or ('y', 'z').

        Raises:
            ValueError: If the specified plane is not supported.
        """
        for obstacle in self.graph.obstacles:
            if plane == ('x', 'y'):
                start = (obstacle['start'][0], obstacle['start'][1])
                size = (obstacle['end'][0] - obstacle['start'][0], obstacle['end'][1] - obstacle['start'][1])
            elif plane == ('y', 'z'):
                start = (obstacle['start'][1], obstacle['start'][2])
                size = (obstacle['end'][1] - obstacle['start'][1], obstacle['end'][2] - obstacle['start'][2])
            else:
                raise ValueError("The plane is not supported.")

            ax.add_patch(plt.Rectangle(start, size[0], size[1], color='red', alpha=0.5))

    def _plot_obstacles_3d(self, ax):
        """
        Plot obstacles in 3D.

        Args:
            ax (matplotlib.axes._subplots.Axes3DSubplot): The Matplotlib 3D axis object.
        """
        for obstacle in self.graph.obstacles:
            x = [obstacle['start'][0], obstacle['end'][0]]
            y = [obstacle['start'][1], obstacle['end'][1]]
            z = [obstacle['start'][2], obstacle['end'][2]]
            ax.bar3d(x[0], y[0], z[0], x[1]-x[0], y[1]-y[0], z[1]-z[0], color='red', alpha=0.5)


class Visualizer2D(Visualizer):
    """
    2D visualizer for creating top-view and side-view plots.

    Inherits from:
        Visualizer
    """

    def plot(self):
        """
        Plot the graph and path in 2D (top view and side view).
        """
        nodes = list(self.graph.nodes)
        edges = self.graph.edges

        # Top view (x-y plane)
        plt.figure(figsize=(10, 5))
        plt.subplot(1, 2, 1)
        plt.title("Top view (x-y plane)")
        for node, neighbors in edges.items():
            for neighbor, _ in neighbors:
                plt.plot([node[0], neighbor[0]], [node[1], neighbor[1]], 'gray', alpha=0.5)
        self._plot_obstacles_2d(plt.gca(), ('x', 'y'))
        path_x, path_y = zip(*[(node[0], node[1]) for node in self.path])
        plt.plot(path_x, path_y, 'blue', label="Path")
        plt.scatter(path_x, path_y, color='blue')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.legend()

        # Side view (y-z plane)
        plt.subplot(1, 2, 2)
        plt.title("Side view (y-z plane)")
        for node, neighbors in edges.items():
            for neighbor, _ in neighbors:
                plt.plot([node[1], neighbor[1]], [node[2], neighbor[2]], 'gray', alpha=0.5)
        self._plot_obstacles_2d(plt.gca(), ('y', 'z'))
        path_y, path_z = zip(*[(node[1], node[2]) for node in self.path])
        plt.plot(path_y, path_z, 'blue', label="Path")
        plt.scatter(path_y, path_z, color='blue')
        plt.xlabel('y')
        plt.ylabel('z')
        plt.legend()

        plt.tight_layout()
        plt.show()


class Visualizer3D(Visualizer):
    """
    3D visualizer for creating a 3D plot of the graph and path.

    Inherits from:
        Visualizer
    """

    def plot(self):
        """
        Plot the graph and path in 3D.
        """
        fig = plt.figure(figsize=(10, 7))
        ax = fig.add_subplot(111, projection='3d')
        ax.set_title("3D plot")

        # Nodes and edges
        for node, neighbors in self.graph.edges.items():
            for neighbor, _ in neighbors:
                ax.plot([node[0], neighbor[0]], [node[1], neighbor[1]], [node[2], neighbor[2]], 'gray', alpha=0.5)

        # Obstacles
        self._plot_obstacles_3d(ax)

        # Path
        path_x, path_y, path_z = zip(*self.path)
        ax.plot(path_x, path_y, path_z, 'blue', label="Path")
        ax.scatter(path_x, path_y, path_z, color='blue')

        ax.set_xlabel('X axis')
        ax.set_ylabel('Y axis')
        ax.set_zlabel('Z axis')
        plt.legend()
        plt.show()
