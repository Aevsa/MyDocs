import os
from dotenv import load_dotenv

load_dotenv()

def get_config_value(key):
    return os.getenv(key)
