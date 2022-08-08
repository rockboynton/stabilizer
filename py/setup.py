from setuptools import setup, find_packages

setup(name="stabilizer",
      packages=find_packages(),
      version="0.1",
      description="Stabilizer Utilities",
      author="QUARTIQ GmbH",
      license="MIT",
      install_requires=[
            "numpy",
            "gmqtt",
            "miniconf-mqtt@git+https://github.com/quartiq/miniconf@develop#subdirectory=py/miniconf-mqtt"
      ])
