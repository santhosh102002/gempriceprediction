from setuptools import setup, find_packages

def get_requirements(file_path:str):
    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n','') for req in requirements]
        return requirements



setup(
    name='DiamondPricePrediction1',
    version='0.0.1',
    author='santhosh',
    author_email='santhosh102002@gmail.com',
    install_requires = get_requirements('requirements.txt'),
    packages=find_packages()
)