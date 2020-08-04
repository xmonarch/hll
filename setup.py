import pathlib

from setuptools import setup

setup(name='hllogs',
      version='0.1.0',
      author='xmonarch',
      author_email='xmonarch64@gmail.com',
      packages=['hllogs'],
      scripts=['bin/hllogs'],
      description="Simple log highlighter",
      long_description=(pathlib.Path(__file__).parent / "README.md").read_text(),
      long_description_content_type="text/markdown",
      install_requires=[],
      license="GPLv2",
      platforms=["Independent"],
      keywords="colorize highlight logs",
      url="https://github.com/xmonarch/hllogs",
      classifiers=[
          "Intended Audience :: Developers",
          "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
          "Programming Language :: Python :: 3.8",
      ]
      )
