from setuptools import setup, find_packages

setup(
    name='module',
    version='1.0.0',
    url='https://github.com/Lpourchot/module.git',
    author='Laurent Pourchot',
    author_email='laurent_pourchot@fr.ibm.com',
    description='module selon les besoins',
    packages=find_packages(),    
    install_requires=['numpy >= 1.11.1'],
    install_requires=read_requirements("requirements.txt"),
)
