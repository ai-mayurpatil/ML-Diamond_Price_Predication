
# Diamond Price Prediction

The dataset for this competition (both train and test) was generated from a deep learning model trained on the Gemstone Price Prediction dataset. Feature distributions are close to, but not exactly the same, as the original. Feel free to use the original dataset as part of this competition, both to explore differences as well as to see whether incorporating the original in training improves model performance.

## Introduction About the Data :

The dataset The goal is to predict price of given diamond (Regression Analysis).

### There are 10 independent variables (including id):


- `id`: unique identifier of each diamond
- `carat` : Carat (ct.) refers to the unique unit of weight measurement used exclusively to weigh gemstones and diamonds.
- `cut` : Quality of Diamond Cut
- `color` : Color of Diamond
- `clarity` : Diamond clarity is a measure of the purity and rarity of the stone, graded by the visibility of these characteristics under 10-power magnification.
- `depth` : The depth of diamond is its height (in millimeters) measured from the culet (bottom tip) to the table (flat, top surface)
- `table` : A diamond's table is the facet which can be seen when the stone is viewed face up.
- `x` : Diamond X dimension
- `y` : Diamond Y dimension
- `x` : Diamond Z dimension

### Target variable:
- `price`: Price of the given Diamond.

Dataset Source Link : https://www.kaggle.com/competitions/playground-series-s3e8/data?select=train.csv

# Project Structure
## 1. Create Virtual Environment
```bash
- conda create -p venv python=3.11
- conda activate "Path"
```
## 2. Create Setup.py file
### `requirements.txt`
```txt
pandas
numpy
seaborn
flask

# Link for setup file and run
#-e .
```
### `setup.py`
```python
# Import Packages
from setuptools import find_packages,setup
from typing import List

## Ignore in requiremets file [-e .]
#HYPEN_E_DOT='-e'

# Function for read requirements file and install
def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        # Condition for remove -e . 
        ##if HYPEN_E_DOT in requirements:
        #    requirements.remove(HYPEN_E_DOT)

        return requirements
    
# Create setup metadata
setup(
    name='Diamond Price Prediction',
    version='0.0.1',
    author='Mayur',
    author_email='ai.mayurpatil@gmail.com',
    install_requires=get_requirements('requirements.txt'),
    packages=find_packages()

    )
```
Run Command:
```bash
python setup.py install
```
## 3. Folders for projects distribution.
### `Folder Structure`
> __Folder Information__
> *  `src\` : Lifecycle of project.
>       *  `src\pipelines` : Here Prediction & Training pipeline.
>       *  `src\components` : Here Data Ingestion, Transformation, Model Trainer.
>       *   _logger_, _exception_, __utils:__ for use all common code and functionality for project file.
> *  `artifacts\` : Preprocessing data store in local.
> * `notebook\data` : All train model.

## 4. Create logging and exception files for project.
### `logger.py`
The code initializes a logging system that writes detailed logs (including timestamps and error levels) to a file named after the current date and time, stored in a logs directory.
```python
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

```
***
### `exception.py`
The code is a framework for handling exceptions in a detailed and structured way, logging specific error information, and raising a custom exception to provide more context about what went wrong.
```python
# Import necessary packages and modules
import sys
from src.logger import logging

# Function to create a detailed error messagee
def error_message_detail(error,error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename

    error_message = "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )

    return error_message

# Custom exception class to handle and log exceptions
class CustomException(Exception):
    
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message  
    
# Entry point of code run
if __name__=="__main__":
    logging.info("Logging has started")

    try:
        a=1/0
    except Exception as e:
        logging.info('Division by zero') 
        raise CustomException(e,sys)
```
Run Command:
```bash
python -m src.exception
```