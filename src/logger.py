# Import necessary packages
import logging 
import os
from datetime import datetime

# Log file name set by date, hour, min, sec
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Define the log directory path
logs_dir = os.path.join(os.getcwd(), "logs")

# Create the log directory if it doesn't exist
os.makedirs(logs_dir, exist_ok=True)

# Define the full log file path
LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)

# Basic configuration for logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
