import logging
from typing import List, Dict

from hllogs.ascii import Ascii


class LogLevelRule:
    """
    Rule describing coloring of items in a line assigned to this log level
    """

    """
    ASCII escapes for coloring the entire output line
    """
    line: str

    """
    ASCII escapes for coloring positive highlighted phrases
    """
    positive: str

    """
    ASCII escapes for coloring negative highlighted phrases
    """
    negative: str

    def __init__(self, line: List[str], positive: List[str], negative: List[str]):
        self.line: str = ''.join(line)
        self.positive: str = ''.join(positive)
        self.negative: str = ''.join(negative)


"""
All registered log level rules
"""
LOG_LEVELS: Dict[int, LogLevelRule] = dict()

"""
Default rule, no specific log level recognized 
"""
LOG_LEVELS[logging.NOTSET] = LogLevelRule(
    [Ascii.END],
    [Ascii.GREEN],
    [Ascii.RED]
)

"""
DEBUG log level
"""
LOG_LEVELS[logging.DEBUG] = LogLevelRule(
    [Ascii.GREEN],
    [Ascii.BLUE],
    [Ascii.RED]
)

"""
INFO log level
"""
LOG_LEVELS[logging.INFO] = LogLevelRule(
    [Ascii.END],
    [Ascii.GREEN],
    [Ascii.RED]
)

"""
WARNING log level
"""
LOG_LEVELS[logging.WARNING] = LogLevelRule(
    [Ascii.YELLOW],
    [Ascii.BOLD, Ascii.GREEN],
    [Ascii.BOLD, Ascii.RED]
)

"""
ERROR log level
"""
LOG_LEVELS[logging.ERROR] = LogLevelRule(
    [Ascii.RED],
    [Ascii.BOLD, Ascii.UNDERLINE, Ascii.GREEN],
    [Ascii.BOLD, Ascii.UNDERLINE, Ascii.YELLOW]
)

"""
FATAL log level
"""
LOG_LEVELS[logging.FATAL] = LogLevelRule(
    [Ascii.BOLD, Ascii.RED],
    [Ascii.BOLD, Ascii.UNDERLINE, Ascii.GREEN],
    [Ascii.BOLD, Ascii.UNDERLINE, Ascii.YELLOW]
)

"""
CRITICAL log level
"""
LOG_LEVELS[logging.CRITICAL] = LogLevelRule(
    [Ascii.UNDERLINE, Ascii.BOLD, Ascii.RED],
    [Ascii.BOLD, Ascii.UNDERLINE, Ascii.GREEN],
    [Ascii.BOLD, Ascii.UNDERLINE, Ascii.YELLOW]
)
