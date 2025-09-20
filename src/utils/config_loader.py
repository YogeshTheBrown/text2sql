import os
from pathlib import Path
import yaml
from dotenv import load_dotenv

# load the .env file
load_dotenv()

def load_config(config_path: str = "config.yaml") -> dict:
    """
    Load YAML config and overlay environment variables if needed.
    """

    config_file = Path(config_path)
    if not config_file.exists():
        raise FileNotFoundError(f"Config file {config_path} not found.")
    
    with open(config_file, 'r') as file:
        config = yaml.safe_load(file) # using the safe_load to prevent code execution vulnerabilities

