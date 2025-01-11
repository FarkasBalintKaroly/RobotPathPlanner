import json


class ConfigLoader:

    def __init__(self):
        self.config = None

    def load_config(self, file_path):
        """Load and validate JSON config file."""
        try:
            with open(file_path, 'r') as file:
                self.config = json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError(f"Config file not found: {file_path}")
        except json.JSONDecodeError:
            raise ValueError(f"Config file is not valid JSON: {file_path}")

        self.validate_config(self.config)
        return self.config

    @staticmethod
    def validate_config(config):
        """Check if nothing is missing."""
        # Check keys
        required_keys = ["space_size", "grid_resolution", "obstacles", "start_point", "goal_point"]
        for key in required_keys:
            if key not in config:
                raise ValueError(f"Missing key in config: {key}")

        # Check space_size
        if not isinstance(config["space_size"], list) or len(config["space_size"]) != 3:
            raise ValueError("The 'space_size' key must contain a 3 element list!")
        if any(dim <= 0 for dim in config["space_size"]):
            raise ValueError("All elements in 'space_size' must be positive!")

        # Check grid resolution
        if not isinstance(config["grid_resolution"], (int, float)) or config["grid_resolution"] <= 0:
            raise ValueError("The 'grid_resolution' must be positive!")

        # Check obstacles
        if not isinstance(config["obstacles"], list):
            raise ValueError("The 'obstacles' key must contain a list of obstacles!")
        for obstacle in config["obstacles"]:
            if "start" not in obstacle or "end" not in obstacle:
                raise ValueError("Each obstacle must have 'start' and 'end' keys!")
            if not isinstance(obstacle["start"], list) or len(obstacle["start"]) != 3:
                raise ValueError("Each obstacle's 'start' must be a 3 element list!")
            if not isinstance(obstacle["end"], list) or len(obstacle["end"]) != 3:
                raise ValueError("Each obstacle's 'end' must be a 3 element list!")
            if any(s > e for s, e in zip(obstacle["start"], obstacle["end"])):
                raise ValueError("Each obstacle's 'start' must be less than or equal to its 'end'!")

        # Check start_point
        if not isinstance(config["start_point"], list) or len(config["start_point"]) != 3:
            raise ValueError("The 'start_point' key must contain a 3 element list!")
        if any(not isinstance(coord, (int, float)) for coord in config["start_point"]):
            raise ValueError("The 'start_point' elements must be numbers!")

        # Check goal_point
        if not isinstance(config["goal_point"], list) or len(config["goal_point"]) != 3:
            raise ValueError("The 'goal_point' key must contain a 3 element list!")
        if any(not isinstance(coord, (int, float)) for coord in config["goal_point"]):
            raise ValueError("The 'goal_point' elements must be numbers!")

        print("Configuration is valid! -- Ready to go.")
