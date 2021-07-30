from setuptools import find_packages, setup
import re
from os.path import join


def get_version():
    with open(join('src', 'moldoc', '__init__.py'), 'r') as f:
        content = f.read()
    p = re.compile(r'^__version__ = [\'"]([^\'\"]*)[\'"]', re.M)
    return p.search(content).group(1)


setup(
    name='moldoc',
    author='Lukas Turcani',
    author_email='lukasturcani93@gmail.com',
    url='https://www.github.com/lukasturcani/moldoc',
    version=get_version(),
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    package_data={
        '': ['*.js'],
    },
    install_requires=(
        'sphinx',
    ),
    python_requires='>=3.7',
)
