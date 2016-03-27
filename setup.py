from setuptools import setup

setup(name='TPpy',
      version='0.1.0',
      packages=['tppy'],
      entry_points={
          'console_scripts': [
              'tppy = tppy.__main__:main'
          ]
      }, requires=['requests']
      )
