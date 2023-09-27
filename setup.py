from setuptools import setup, find_packages

setup(
    name='EDA_TerroristAttack',
    version='0.1',
    packages=find_packages(),
    install_requires=[
       'pandas==1.5.3',
       'matplotlib==3.7.0',
       'seaborn==0.12.2',
       'python==3.11'
    ],
)
