import logging
import os
from datetime import datetime

# Define log file path with timestamp
LOG_FILE_PATH = os.path.join("logs", f"{datetime.now():%Y-%m-%d_%H-%M-%S}.log")
os.makedirs("logs", exist_ok=True)

# Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
