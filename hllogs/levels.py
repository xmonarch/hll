import logging
from typing import List, Dict

from hllogs.ascii import Ascii


class LogLevelRule:

    def __init__(self, line: List[str], positive: List[str], negative: List[str]):
        self.line: str = ''.join(line)
        self.positive: str = ''.join(positive)
        self.negative: str = ''.join(negative)


LOG_LEVELS: Dict[int, LogLevelRule] = dict()

LOG_LEVELS[logging.INFO] = LogLevelRule(
    [Ascii.END],
    [Ascii.GREEN],
    [Ascii.BOLD, Ascii.RED]
)

LOG_LEVELS[logging.DEBUG] = LogLevelRule(
    [Ascii.GREEN],
    [Ascii.BOLD, Ascii.BLUE],
    [Ascii.BOLD, Ascii.RED]
)

LOG_LEVELS[logging.WARNING] = LogLevelRule(
    [Ascii.YELLOW],
    [Ascii.BOLD, Ascii.GREEN],
    [Ascii.BOLD, Ascii.RED]
)

LOG_LEVELS[logging.ERROR] = LogLevelRule(
    [Ascii.RED],
    [Ascii.BOLD, Ascii.UNDERLINE, Ascii.GREEN],
    [Ascii.BOLD, Ascii.UNDERLINE, Ascii.YELLOW]
)

LOG_LEVELS[logging.FATAL] = LogLevelRule(
    [Ascii.BOLD, Ascii.RED],
    [Ascii.BOLD, Ascii.UNDERLINE, Ascii.GREEN],
    [Ascii.BOLD, Ascii.UNDERLINE, Ascii.YELLOW]
)

LOG_LEVELS[logging.CRITICAL] = LogLevelRule(
    [Ascii.UNDERLINE, Ascii.BOLD, Ascii.RED],
    [Ascii.BOLD, Ascii.UNDERLINE, Ascii.GREEN],
    [Ascii.BOLD, Ascii.UNDERLINE, Ascii.YELLOW]
)
