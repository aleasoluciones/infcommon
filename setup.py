from setuptools import setup, find_packages

setup(name='infcommon',
      version='0.0.1',
      author='Bifer Team',
      description ='felix platform common infrastructure',
      platforms = 'Linux',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests'])
      )

