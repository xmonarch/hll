from typing import List

from hllogs.ascii import Ascii


class LogLevelRule:

    def __init__(self, contains: List[str], ascii_escapes: List[str]):
        self.contains: List[str] = contains
        self.ascii_escapes: str = ''.join(ascii_escapes)

    def matches(self, line: str):
        for contain in self.contains:
            if contain in line:
                return True


RULES: List[LogLevelRule] = [
    LogLevelRule(['critical'], [Ascii.UNDERLINE, Ascii.BOLD, Ascii.RED]),
    LogLevelRule(['fatal'], [Ascii.BOLD, Ascii.RED]),
    LogLevelRule(['error', ' e '], [Ascii.RED]),
    LogLevelRule(['warn', ' w '], [Ascii.YELLOW]),
    LogLevelRule(['debug', ' d '], [Ascii.GREEN]),
]

DEFAULT_RULE = LogLevelRule([], [Ascii.END])
