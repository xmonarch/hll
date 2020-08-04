import sys
from typing import List


class AsciiEscape:
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    BLINK = '\033[5m'
    REVERSE = '\033[7m'
    BLACK = '\033[90m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    HIGHLIGHT = BOLD + UNDERLINE


class HighlightRule:

    def __init__(self, contains: List[str], ascii_escapes: List[str]):
        self.contains: List[str] = contains
        self.ascii_escapes: str = ''.join(ascii_escapes)

    def matches(self, line: str):
        for contain in self.contains:
            if contain in line:
                return True


log_level_rules: List[HighlightRule] = [
    HighlightRule(['critical'], [AsciiEscape.UNDERLINE, AsciiEscape.BLINK, AsciiEscape.BOLD, AsciiEscape.RED]),
    HighlightRule(['fatal'], [AsciiEscape.BOLD, AsciiEscape.RED]),
    HighlightRule(['error', ' e '], [AsciiEscape.RED]),
    HighlightRule(['warn', ' w '], [AsciiEscape.YELLOW]),
    HighlightRule(['info', ' o '], [AsciiEscape.END]),
    HighlightRule(['debug', ' d '], [AsciiEscape.GREEN]),
]

default_rule = HighlightRule([], [AsciiEscape.END])

keywords: List[str] = [
    'failed',
    'oracle',
    'failed',
    'critical',
    'fatal',
    'error,'
    'warning',
    'info',
    'debug'
]


def highlight():
    try:
        while True:
            line_rule = default_rule
            try:
                line: str = input()
                line_lower: str = line.lower()
                for rule in log_level_rules:
                    if rule.matches(line_lower):
                        line_rule = rule
                        break
                for keyword in keywords:
                    if keyword in line:
                        line = line.replace(keyword,
                                            AsciiEscape.HIGHLIGHT + keyword + AsciiEscape.END + line_rule.ascii_escapes)
                print(line_rule.ascii_escapes + line + AsciiEscape.END)
            except EOFError:
                break
    except KeyboardInterrupt:
        sys.exit(0)
