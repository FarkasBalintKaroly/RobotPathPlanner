import json


class ConfigLoader:
    """
    Class to load and validate a JSON configuration file for a 3D path planner.

    Attributes:
        config (dict): The loaded configuration file as a dictionary.
    """

    def __init__(self):
        """
        Initialize the ConfigLoader with no configuration loaded.
        """
        self.config = None

    def load_config(self, file_path):
        """
        Load and validate a JSON config file.

        Args:
            file_path (str): The path to the configuration file.

        Returns:
            dict: The validated configuration.

        Raises:
            FileNotFoundError: If the configuration file does not exist.
            ValueError: If the file is not valid JSON or the configuration is invalid.
        """
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
        """
        Validate the contents of a configuration file.

        Args:
            config (dict): The configuration dictionary.

        Raises:
            ValueError: If any validation check fails.

        Validation Checks:
            - Required keys must be present.
            - `space_size` must be a list of 3 positive numbers.
            - `grid_resolution` must be a positive number.
            - `obstacles` must be a list of valid obstacle dictionaries.
            - `start_point` must be a list of 3 numeric values.
            - `goal_point` must be a list of 3 numeric values.
        """

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
