from setuptools import find_packages, setup

setup(
    name='litplyot',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'matplotlib',
        'seaborn',
        'pandas',
    ],
)