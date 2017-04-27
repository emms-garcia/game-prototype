# -*- coding: utf-8 -*-
from setuptools import setup


with open('README.md') as f:
    README = f.read()

with open('requirements.txt') as f:
    REQUIREMENTS = list(map(str.strip, f.readlines()))

setup(
    author='Emmanuel García',
    author_email='emmanuel.garcia.solis@gmail.com',
    description='Game prototype just for fun.',
    entry_points={
        'console_scripts': [
            'game = game.game:main',
        ],
    },
    install_requires=REQUIREMENTS,
    license='MIT',
    long_description=README,
    name='game',
    packages=['game'],
    scripts=[],
    url='https://github.com/synnick/game-prototype',
    version='0.1',
)
