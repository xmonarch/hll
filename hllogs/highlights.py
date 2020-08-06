import logging
import re
from re import Pattern
from typing import List


class Highlighter(object):
    """
    Configuration of a single highlighter object
    """

    """
    Regular expression for matching tokens in a string
    """
    expression: Pattern

    """
    Requested log level of the tokens produced by the highlighter
    """
    raise_level: int

    """
    Defined whether this highlighter produces positive or negative tokens
    """
    positive: bool

    def __init__(self, expression: Pattern, raise_level: int = logging.NOTSET, positive: bool = False):
        self.expression = expression
        self.raise_level = raise_level
        self.positive = positive


"""
List of all registered highlighters
"""
LOG_HIGHLIGHTERS: List[Highlighter] = [
    # URLs
    Highlighter(re.compile(r"\w+://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*(),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"), positive=True),
    # key phrases
    Highlighter(re.compile('unsuccessfully', re.IGNORECASE)),
    Highlighter(re.compile('disconnected', re.IGNORECASE)),
    Highlighter(re.compile('unsuccessful', re.IGNORECASE)),
    Highlighter(re.compile('successfully', re.IGNORECASE), positive=True),
    Highlighter(re.compile('uninstalled', re.IGNORECASE)),
    Highlighter(re.compile('installing', re.IGNORECASE), positive=True),
    Highlighter(re.compile('dismounted', re.IGNORECASE)),
    Highlighter(re.compile('successful', re.IGNORECASE), positive=True),
    Highlighter(re.compile('connected', re.IGNORECASE), positive=True),
    Highlighter(re.compile('installed', re.IGNORECASE), positive=True),
    Highlighter(re.compile('disabling', re.IGNORECASE)),
    Highlighter(re.compile('completed', re.IGNORECASE), positive=True),
    Highlighter(re.compile('exception', re.IGNORECASE), raise_level=logging.ERROR),
    Highlighter(re.compile('enabling', re.IGNORECASE), positive=True),
    Highlighter(re.compile('critical', re.IGNORECASE), raise_level=logging.CRITICAL),
    Highlighter(re.compile('starting', re.IGNORECASE), positive=True),
    Highlighter(re.compile('disabled', re.IGNORECASE)),
    Highlighter(re.compile('stopping', re.IGNORECASE)),
    Highlighter(re.compile('shutdown', re.IGNORECASE)),
    Highlighter(re.compile('enabled', re.IGNORECASE), positive=True),
    Highlighter(re.compile('warning', re.IGNORECASE), raise_level=logging.WARNING),
    Highlighter(re.compile('started', re.IGNORECASE), positive=True),
    Highlighter(re.compile('stopped', re.IGNORECASE)),
    Highlighter(re.compile('missing', re.IGNORECASE), raise_level=logging.WARNING),
    Highlighter(re.compile('cannot', re.IGNORECASE), raise_level=logging.WARNING),
    Highlighter(re.compile('severe', re.IGNORECASE), raise_level=logging.ERROR),
    Highlighter(re.compile('failed', re.IGNORECASE), raise_level=logging.WARNING),
    Highlighter(re.compile('closed', re.IGNORECASE)),
    Highlighter(re.compile('fatal', re.IGNORECASE), raise_level=logging.FATAL),
    Highlighter(re.compile('error', re.IGNORECASE), raise_level=logging.ERROR),
    Highlighter(re.compile('debug', re.IGNORECASE), raise_level=logging.DEBUG),
    # various standard log level descriptions
    Highlighter(re.compile(r'\(II\)'), raise_level=logging.INFO),
    Highlighter(re.compile(r'\(WW\)'), raise_level=logging.WARNING),
    Highlighter(re.compile(r'\(EE\)'), raise_level=logging.ERROR),
    # ORACLE codes
    Highlighter(re.compile(r'ORA-\d+'))
]
