import os
import shutil
from dotenv import load_dotenv
from roboflow import Roboflow

load_dotenv()

ROBO_API_KEY = os.environ.get("ROBO_API_KEY")

#create a Roboflow instance
rf = Roboflow(api_key=ROBO_API_KEY)
#create a Roboflow instance project
project = rf.workspace("roboflow-jvuqo").project("football-players-detection-3zvbc")
#create a project version
version = project.version(1)
#download the Roboflow dataset that will be used for training
dataset = version.download("yolov5")
#reformat data for Roboflow workflow
shutil.move('football-players-detection-1/train', 'football-players-detection-1/football-players-detection-1/train')
shutil.move('football-players-detection-1/test', 'football-players-detection-1/football-players-detection-1/test')
shutil.move('football-players-detection-1/valid', 'football-players-detection-1/football-players-detection-1/valid')

#training was performed by running the command below
# !yolo task=detect mode=train model=yolov5x.pt data={dataset.location}/data.yaml epochs=100 imgsz=640