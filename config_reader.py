import ujson as json

def read_config():
    try:
        with open('config.json', 'r') as f:
            config = json.load(f)
        return config
    except Exception as e:
        # Handle error, e.g., print to console or log
        print(f"Config file error: {e}")
        return None
