import logging
import re
from re import Pattern
from typing import List


class Highlight(object):
    expression: Pattern
    raise_level: int
    positive: bool

    def __init__(self, expression: Pattern, raise_level: int = logging.NOTSET, positive: bool = False):
        self.expression = expression
        self.raise_level = raise_level
        self.positive = positive


LOG_HIGHLIGHTS: List[Highlight] = [
    Highlight(re.compile('disconnected', re.IGNORECASE)),
    Highlight(re.compile('successfully', re.IGNORECASE), positive=True),
    Highlight(re.compile('installing', re.IGNORECASE), positive=True),
    Highlight(re.compile('dismounted', re.IGNORECASE)),
    Highlight(re.compile('connected', re.IGNORECASE), positive=True),
    Highlight(re.compile('installed', re.IGNORECASE), positive=True),
    Highlight(re.compile('disabling', re.IGNORECASE)),
    Highlight(re.compile('completed', re.IGNORECASE), positive=True),
    Highlight(re.compile('exception', re.IGNORECASE), raise_level=logging.ERROR),
    Highlight(re.compile('critical', re.IGNORECASE), raise_level=logging.CRITICAL),
    Highlight(re.compile('starting', re.IGNORECASE), positive=True),
    Highlight(re.compile('disabled', re.IGNORECASE)),
    Highlight(re.compile('stopping', re.IGNORECASE)),
    Highlight(re.compile('shutdown', re.IGNORECASE)),
    Highlight(re.compile('warning', re.IGNORECASE), raise_level=logging.WARNING),
    Highlight(re.compile('started', re.IGNORECASE), positive=True),
    Highlight(re.compile('stopped', re.IGNORECASE)),
    Highlight(re.compile('missing', re.IGNORECASE)),
    Highlight(re.compile('failed', re.IGNORECASE)),
    Highlight(re.compile('closed', re.IGNORECASE)),
    Highlight(re.compile('fatal', re.IGNORECASE), raise_level=logging.FATAL),
    Highlight(re.compile('error', re.IGNORECASE), raise_level=logging.ERROR),
    Highlight(re.compile('debug', re.IGNORECASE), raise_level=logging.DEBUG),
    Highlight(re.compile(r'ORA-\d+'))
]
