import json


class ConfigLoader:

    def load_config(self, file_path):
        """Load and validate JSON config file."""
        with open(file_path, 'r') as file:
            config = json.load(file)
        self.validate_config(config)
        return config

    @staticmethod
    def validate_config(config):
        """Check if nothing is missing."""
        # Check keys
        required_keys = ["space_size", "grid_resolution", "obstacles", "start_point", "goal_point"]
        for key in required_keys:
            if key not in config:
                raise ValueError(f"Missing key in config: {key}")

        # Check values
        if not isinstance(config["space_size"], list) or len(config["space_size"]) != 3:
            raise ValueError("The 'space_size' key must contain a 3 element list!")
        if config["grid_resolution"] <= 0:
            raise ValueError("The 'grid_resolution' must be positive!")
        if not isinstance(config["start_point"], list) or len(config["start_point"]) != 3:
            raise ValueError("The 'start_point' key must contain a 3 element list!")
        if not isinstance(config["goal_point"], list) or len(config["goal_point"]) != 3:
            raise ValueError("The 'goal_point' key must contain a 3 element list!")

        print("Configuration is valid! -- Ready to go.")
