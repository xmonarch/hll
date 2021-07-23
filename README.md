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

```shell
$ git clone https://github.com/xmonarch/hll.git
$ cd hll
$ pip install --user .
```

## Usage

Pipe any input in:

```shell
$ tail -f ~/somelogfile.log | hll
```

For more details run:

```shell
$ hll --help
```
