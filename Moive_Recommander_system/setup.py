from setuptools import find_packages,setup
from typing import List # Tells Python (and other developers) that the function will return a List of strings.

HYPEN_E_DOT="-e ."

def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    Function takes one argument: the path to the requirements file.
    Returns a list of strings (dependencies).

    '''

    requirements=[]
    with open(file_path)as file_obj: #Opens the file safely (context manager ensures it closes after use).
        requirements=file_obj.readlines() # reads all lines from file into a list.
        requirements=[req.replace("\n","")for req in requirements] # removes whitespace & \n

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements # Checks if -e . is in the list. If yes, removes it.


setup(
    name="Movie Recommendation System",
    version="0.0.1",
    author="Vivek",
    author_email="viveksasane99@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)

# that automatically discovers all Python packages (directories with __init__.py) in your project.
# This way, you don’t have to manually list them in setup.py.