from setuptools import find_packages, setup
from typing import List

setup_constant = '-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    this fucntion is used to return the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines() #read the object
        requirements = [req.replace("\n", "") for req in requirements] #replace the \n in requirements.txt with blank

        if setup_constant in requirements:
            requirements.remove(setup_constant)

    return requirements



setup(
name = 'ML_End-to-End',
version = '0.0.1',
author= 'Dutt',
author_email= 'duttlodagala@gmail.com',
packages= find_packages(), #looks for all the __init__py to build the package
install_requires = get_requirements('requirements.txt')

)