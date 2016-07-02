try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

with open('README.rst') as f:
    readme= f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    description= 'My Project',
    author='My Name',
    url='URL to get it at',
    download_url='Where to download it',
    author='Jozef Kovac',
    author_email='mr@jozefkovac.name',
    version='0.1',
    packages=find_packages(exclude=('tests', 'docs')),
    scripts= [],
    name= projectname,
    license= license
)
