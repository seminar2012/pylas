from setuptools import setup, find_packages

setup(
    name='pylas',
    version='0.1',
    description='Las/Laz in python',
    url='https://github.com/tmontaigu/pylas',
    author='Thomas Montaigu',
    # license='MIT',
    packages=find_packages(exclude=('tests',)),
    zip_safe=False
)