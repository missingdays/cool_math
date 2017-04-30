
from distutils.core import setup
from setuptools import find_packages

try:
    import pypandoc
    long_description=pypandoc.convert('README.md', 'rst')
except(IOError, ImportError):
    with open('README.md') as f:
        long_description = f.read()

print(long_description)

setup(
    name='cool_math',
    packages=find_packages(exclude=['test', '*.test', '*.test.*']),
    version='1.4',
    description='Cool math',
    long_description=long_description,
    author='missingdays',
    author_email='rebovykin@gmail.com',
    url='https://github.com/missingdays/cool_math',
    download_url='https://github.com/missingdays/cool_math/archive/1.4.tar.gz',
    keywords=['math'],
    scripts=['bin/cool_math'],
    install_requires=['scipy']
)
