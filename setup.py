from distutils.core import setup
from os import path

_here = path.dirname(path.abspath(__file__))

setup(
    name='config_merger',
    description='Tools for merging data structures from a range of data sources',
    version='0.0.1',
    py_modules=['config_merger'],
    #packages=['foldername'],
    long_description=open(path.join(_here, 'README.md')).read(),

    url='http://git.int.thisisglobal.com/interactive/config-merger',
    author='Global',
    author_email='leicestersquare-interactive-developers@global.com',
    license='MIT',
    platform='any',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords='configuration config merge json yaml url api'
)
