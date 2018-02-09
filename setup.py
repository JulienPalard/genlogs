#!/usr/bin/env python

from distutils.core import setup

setup(name='genlogs',
      version='0.2',
      description='Generate logs according to given distributiosn',
      author='Julien Palard',
      author_email='julien@palard.fr',
      packages=['gen_logs'],
      package_dir={'gen_logs': 'src/gen_logs'},
      entry_points={
          'console_scripts': ['genlogs=gen_logs.gen_logs:main'],
      }
)
