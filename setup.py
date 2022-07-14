from setuptools import find_packages, setup

setup(
  name='react-cli',
  version='0.0.0',
  packages=find_packages(),
  install_requires=[
      'click'
  ],
  entry_points='''
  [console_scripts]
  react-cli=reactcli:reactcli
  '''
)
