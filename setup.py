from distutils.core import setup

long_desc = """
A library of 2-D circle fitting algorithms. Implements a range of algorithms from a simple least-squares algorithm to
a state-of-the-art hyper-fitting algorithm.
"""

version = '0.2.0'

setup(
    name='circle-fit',
    version=version,
    description='Circle Fitting Library in Python',
    long_description=long_desc,
    author='Michael Klear',
    author_email='michael.r.klear@gmail.com',
    url='https://github.com/AlliedToasters/circle-fit',
    install_requires=[
        'numpy >= 1.22.0',
        'scipy',
        'matplotlib'
    ],
    packages=['circle_fit']
)
