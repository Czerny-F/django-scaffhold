import os
from setuptools import find_packages, setup


# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

# with open('requirements.txt') as requirements_file:
#     install_requirements = requirements_file.read().splitlines()

setup(
    name='django-scaffold',
    version='0.1.1',
    description='Dummy Django project for Template frame layout.',
    url='https://github.com/Czerny-F/django-scaffold',
    author='Czerny-F',
    author_email='dummy00.cz@gmail.com',
    packages=find_packages(),
    # install_requires=install_requirements,
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
    ],
)
