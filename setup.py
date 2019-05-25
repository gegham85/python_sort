from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(
    name='sortcollection',
    version='0.2',
    description='This is a package with different sorting algorithms',
    long_description=readme(),
    url='https://github.com/gegham85/python_sort',
    author='Gegham Movses',
    author_email='gegham.movses@gmail.com',
    license='MIT',
    packages=['sortcollection'],
    install_requires=[],
    include_package_data=True,
    zip_safe=False
)