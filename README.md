
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

```bash
- python setup.py install
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