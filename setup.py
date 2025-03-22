from setuptools import setup, find_packages

setup(
    name='meow-cli',
    version='1.0.0',
    author='Miku',
    description='A simple cat command copy',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'meow=meow:main',  
        ],
    },
    classifiers=[
       'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)

