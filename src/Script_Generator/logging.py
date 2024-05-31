import logging
import os
from datetime import datetime

LOG_FILE=f'{datetime.now().strftime("%m_%d_%Y_%H_%M_%S")}.log' #filename

log_path=os.path.join(os.getcwd(),"logs")

os.makedirs(log_path,exist_ok=True) #Create log folder

LOG_FILEPATH=os.path.join(log_path,LOG_FILE) #Inserting log to log folder

logging.basicConfig(level=logging.INFO,
filename=LOG_FILEPATH,
format="[%(asctime)s] %(lineno)d %(name)s -%(levelname)s - %(message)s")