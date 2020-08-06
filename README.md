# hllogs

hllogs (`h`igh`l`ight `logs`) is a simple log colorizer and highlighter written in python.

Features:
- attempt basic log level auto-detection
- highlight key phrases
- extract and pretty-print logged XML and JSON documents

## Screenshots

TBD

## Installation

`$ git clone https://github.com/xmonarch/hllogs.git`

`$ cd hllogs`

`$ sudo pip install .`

## Usage

Pipe any input in:

`$ tail -f ~/somelogfile.log | hllogs`

## TODO

- fix empty lines breaking hllogs
