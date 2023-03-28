from setuptools import find_packages,setup
from typing import List
hypen="-e ."
def get_requirements(file_path:str) -> List[str]:
    '''
    this function will return the list of the Requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
         requirements=file_obj.readlines()
         requirements=[req.replace('\n','') for req in requirements]
         if hypen in requirements:
              requirements.remove(hypen)
    return requirements


setup(
    name='mlproject',
    version='0.0.1', 
    author='Akash', 
    author_email='akash.dasp@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)