from distutils.core import setup

long_desc = """
A simple library for fitting circles to data in 2-D space. Impliments a simple least-squares solver and the state-of-the-art "hyper-fit" algorithm (https://www.sciencedirect.com/science/article/pii/S0167947310004809?via%3Dihub) in python.
"""

version = '0.1.3'

setup(
    name='circle-fit',
    version=version,
    description='Circle Fitting Library in Python',
    long_description=long_desc,
    author='Michael Klear',
    author_email='michael.r.klear@gmail.com',
    url='https://github.com/AlliedToasters/circle-fit/archive/v0.1.2.tar.gz',
    install_requires=[
        'numpy',
        'scipy',
        'matplotlib'
    ],
    packages=['circle_fit']
)
