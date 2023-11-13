
from setuptools import setup, find_packages

setup(
    name='math_quiz',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # list your package's dependencies here
    ],
    entry_points={
        'console_scripts': [
            'math_quiz = math_quiz:main',
        ],
    },
    author='Nishant Mishra',
    description='DSSS Homework 2',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/nish-nm/dsss_homework_2',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
