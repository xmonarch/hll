from typing import List

from hllogs.ascii import Ascii


class LogLevelRule:

    def __init__(self, contains: List[str], line_escapes: List[str], highlight_escapes: List[str]):
        self.contains: List[str] = contains
        self.line_escapes: str = ''.join(line_escapes)
        self.highlight_escapes: str = ''.join(highlight_escapes)

    def matches(self, line: str):
        for contain in self.contains:
            if contain in line:
                return True


RULES: List[LogLevelRule] = [
    LogLevelRule(['critical'], [Ascii.UNDERLINE, Ascii.BOLD, Ascii.RED], [Ascii.BOLD, Ascii.UNDERLINE, Ascii.YELLOW]),
    LogLevelRule(['fatal'], [Ascii.BOLD, Ascii.RED], [Ascii.BOLD, Ascii.UNDERLINE, Ascii.YELLOW]),
    LogLevelRule(['error', ' e '], [Ascii.RED], [Ascii.BOLD, Ascii.UNDERLINE, Ascii.YELLOW]),
    LogLevelRule(['warn', ' w '], [Ascii.YELLOW], [Ascii.BOLD, Ascii.RED]),
    LogLevelRule(['debug', ' d '], [Ascii.GREEN], [Ascii.BOLD, Ascii.YELLOW]),
]

DEFAULT_RULE = LogLevelRule([], [Ascii.END], [Ascii.BOLD, Ascii.BLUE])
