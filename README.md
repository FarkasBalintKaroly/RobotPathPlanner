# RobotPathPlanner

<hr>

> ## Overview

The RobotPathPlanner project is a Python-based 3D path planning tool designed to find the shortest route for a robot to navigate a 3D space with obstacles. The project includes graph generation, pathfinding algorithms, and visualization features.

<hr>

> ## Features

1. Configuration Handling:
   - Reads and validates a JSON configuration file containing space size, grid resolution, obstacles, start, and goal points.
2. Graph Generation:
   - Creates a 3D grid-based graph, removing nodes that intersect with obstacles.
   - Calculates connections between neighboring nodes.
3. Path Planning:
   - Uses Dijkstra's algorithm to compute the shortest path between the start and goal nodes.
4. Visualization:
   - Supports both 2D and 3D visualizations of the graph, obstacles, and the planned path.

<hr>

> ## Installation

1. Clone the repository.
    ```
    git clone https://github.com/FarkasBalintKaroly/RobotPathPlanner.git
    cd RobotPathPlanner
    ```
2. Install the dependencies.
    ```
    pip install -r requirements.txt
    ```
3. Run the program.
    ```
    python main.py
    ```

<hr>

> ## Configuration

Create a JSON configuration file with the following structure:
```json
{
  "space_size": [1.0, 1.0, 1.0],
  "grid_resolution": 0.1,
  "obstacles": [
    {
      "start": [0.2, 0.2, 0.2],
      "end": [0.4, 0.4, 0.4]
    },
    {
      "start": [0.6, 0.6, 0.6],
      "end": [0.8, 0.8, 0.8]
    }
  ],
  "start_point": [0, 0, 0],
  "goal_point": [1, 1, 1]
}
```

<hr>

> ## Activity Diagram

<img src="https://github.com/FarkasBalintKaroly/RobotPathPlanner/blob/main/assets/Activity-diagram.png?raw=true" align="center">

<hr>

> ## Class Diagram

<img src="https://github.com/FarkasBalintKaroly/RobotPathPlanner/blob/main/assets/UML-class-diagram.png?raw=true" align="center">

<hr>

> ## Future Enhancements
1. Implement A* algorithm for more efficient pathfinding.
2. Add support for dynamic obstacle handling.
3. Integrate a graphical user interface (GUI).

<hr>