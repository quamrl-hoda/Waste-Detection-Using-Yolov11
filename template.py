import os
from pathlib import Path
import logging


logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(levelname)s - %(message)s')

project_name = "wasteDetection"

list_of_files = [
  ".github/workflows/.gitkeep",
  f"src/{project_name}/__init__.py",
  f"src/{project_name}/components/__init__.py",
  f"src/{project_name}/components/data_ingestion.py",
  f"src/{project_name}/components/data_validation.py",
  f"src/{project_name}/components/model_trainer.py",
  f"src/{project_name}/utils/__init__.py",
  f"src/{project_name}/utils/common.py",
  f"src/{project_name}/constants/__init__.py",
  f"src/{project_name}/constants/application.py",
  f"src/{project_name}/entity/__init__.py",
  f"src/{project_name}/entity/config_entity.py",
  f"src/{project_name}/pipeline/__init__.py",
  f"src/{project_name}/pipeline/training_pipeline.py",
  f"src/{project_name}/logger.py",
  f"src/{project_name}/exception/__init__.py",
  f"src/{project_name}/exception/custom_exception.py",
  f"src/{project_name}/config/__init__.py",
  f"src/{project_name}/config/configuration.py",

  "config/config.yaml",
  "params.yaml",
  "requirements.txt",
  "setup.py",
  "research/trials.ipynb",
  "Dockerfile",
  "app.py",
  "main.py",
  "dvc.yaml",
  ".dvcignore"
   
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Created directory: {filedir}") 
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
        logging.info(f"Created file: {filepath}")
    else:
        logging.info(f"File already exists and is not empty: {filepath}")