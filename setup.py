from setuptools import setup, find_packages

setup(name='infcommon',
      version='0.0.1',
      author='Bifer Team',
      description='Common Infrastructure Utilities',
      platforms='Linux',
      packages=find_packages(exclude=['ez_setup',
                                      'examples',
                                      'tests',
                                      'specs',
                                      'integration_specs']),
      install_requires=['sentry-sdk==1.1.0',
                        'retrying==1.3.3',
                        'PyYAML==4.2b4',
                        'jsonpickle==0.5.0',
                        'six>=1.13.0',
                        ]
      )

