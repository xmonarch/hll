import sys

from hllogs.ascii import Ascii
from hllogs.highlights import HIGHLIGHTS
from hllogs.levels import DEFAULT_RULE, RULES


def process():
    try:
        while True:
            line_rule = DEFAULT_RULE
            try:
                line: str = input()
                line_lower: str = line.lower()
                for rule in RULES:
                    if rule.matches(line_lower):
                        line_rule = rule
                        break
                for highlight in HIGHLIGHTS:
                    if highlight in line:
                        line = line.replace(highlight,
                                            Ascii.HIGHLIGHT + highlight + Ascii.END + line_rule.ascii_escapes)
                print(line_rule.ascii_escapes + line + Ascii.END)
            except EOFError:
                break
    except KeyboardInterrupt:
        sys.exit(0)

# TODO case-insensitive highlights replace
# TODO reg-exp highlights
