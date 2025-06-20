import os

def load_config_from_env_file(app, path):
    """
    Manually reads a .env file and loads its key-value pairs
    into the Flask app.config.
    """
    print(f"--- Manually loading config from: {path} ---")
    try:
        with open(path) as f:
            for line in f:
                # Ignore comments and empty lines
                if line.startswith('#') or not line.strip():
                    continue
                
                # Split the line into key and value
                key, value = line.strip().split('=', 1)
                
                # Remove quotes from the value if they exist
                value = value.strip().strip("'\"")
                
                # Load into app.config dictionary
                app.config[key] = value
                print(f"Loaded: {key} = {value}")

    except FileNotFoundError:
        print(f"FATAL: .env file not found at {path}")
    except Exception as e:
        print(f"FATAL: Error reading .env file: {e}")