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