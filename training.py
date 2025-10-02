import os
import shutil
from dotenv import load_dotenv
from roboflow import Roboflow

load_dotenv()

ROBO_API_KEY = os.environ.get("ROBO_API_KEY")