# hll

hll (`h`igh`l`ight `l`ogs) is a simple log colorizer and highlighter written in python.

Features:
- attempts basic log level auto-detection and colorizes output accordingly
- highlights key phrases in the output
- extracts and pretty-prints logged XML and JSON documents

## Screenshot

Terminal running with [nord theme](https://www.nordtheme.com/). Various coloring 
for different log levels. JSON and XML documents embedded in log messages are
extracted and pretty printed for easier inspection.

![Sample](/screenshots/sample.png)

## Installation

`$ git clone https://github.com/xmonarch/hll.git`

`$ cd hll`

`$ sudo pip install .`

## Usage

Pipe any input in:

`$ tail -f ~/somelogfile.log | hll`

For more details run:

`$ hll --help`
