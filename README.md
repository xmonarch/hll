# hllogs

hllogs (`h`igh`l`ight `logs`) is a simple log colorizer and highlighter written in python.

Features:
- attempts basic log level auto-detection and colorizes output accordingly
- highlights key phrases in the output
- extracts and pretty-prints logged XML and JSON documents

## Screenshot

![Sample](/screenshots/sample.png)

## Installation

`$ git clone https://github.com/xmonarch/hllogs.git`

`$ cd hllogs`

`$ sudo pip install .`

## Usage

Pipe any input in:

`$ tail -f ~/somelogfile.log | hllogs`
