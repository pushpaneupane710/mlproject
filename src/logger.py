import logging
import os
from datetime import datetime

# Create log file name (safe for all OS)
LOG_FILE = f"{datetime.now().strftime('%d-%m-%Y_%H-%M-%S')}.log"

# Create logs directory path
logs_path = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_path, exist_ok=True)

# Full log file path
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Logging configuration
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

'''
if __name__ == "__main__":
    
    try:
        a=1/0
    except Exception as e:
        logging.info("Divide by zero")    
        #logging.info("Logging has started")
        raise CustomException(e,sys)
'''
    