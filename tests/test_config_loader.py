from src.config_loader import ConfigLoader


def test_load_config():
    loader = ConfigLoader()
    config = loader.load_config("../config/default_config.json")
    print(config)


test_load_config()
