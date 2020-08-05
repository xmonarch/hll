import sys
from re import Pattern
from typing import List

from hllogs.ascii import Ascii
from hllogs.highlights import HIGHLIGHTS
from hllogs.levels import DEFAULT_RULE, RULES, LogLevelRule


class Item(object):

    def __init__(self, value: str, is_token: bool = False):
        self.value: str = value
        self.is_token = is_token


def highlight(value: str, escape: str, line_escapes: str) -> str:
    return f"{escape}{value}{Ascii.END}{line_escapes}"


def split(expression: Pattern, value: str) -> List[Item]:
    results: List[Item] = []
    position: int = 0
    matched: bool = False
    for match in expression.finditer(value):
        matched = True
        if position < match.start():
            results.append(Item(value[position:match.start()]))
        results.append(Item(value[match.start():match.end()], is_token=True))
        position = match.end()
    if matched and position < len(value):
        results.append(Item(value[position:]))

    return results


def tokenize(item: Item) -> List[Item]:
    length: int = len(item.value)
    if item.is_token or length < 4:
        return [item]
    tokenized = []
    for expression in HIGHLIGHTS:
        parts = split(expression, item.value)
        if len(parts) > 0:
            for part in parts:
                if part.is_token:
                    tokenized.append(part)
                else:
                    tokenized.extend(tokenize(part))
            break
    return tokenized if len(tokenized) > 0 else [item]


def join(tokens: List[Item], line: LogLevelRule) -> str:
    complete: str = ''
    for token in tokens:
        complete += highlight(token.value, line.highlight_escapes, line.line_escapes) if token.is_token else token.value
    return complete


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
                print(highlight(join(tokenize(Item(line)), line_rule), line_rule.line_escapes, ''))
            except EOFError:
                break
    except KeyboardInterrupt:
        sys.exit(0)
