import logging
import sys
from typing import List

from hllogs.ascii import Ascii
from hllogs.highlights import LOG_HIGHLIGHTS, Highlight
from hllogs.levels import LOG_LEVELS, LogLevelRule


class Item(object):

    def __init__(self, value: str, is_token: bool = False, raise_level: int = logging.INFO, is_positive: bool = False):
        self.value: str = value
        self.is_token: bool = is_token
        self.raise_level: int = raise_level
        self.is_positive: bool = is_positive


def highlight(value: str, escape: str, line_escapes: str) -> str:
    return f"{escape}{value}{Ascii.END}{line_escapes}"


def split(expression: Highlight, value: str) -> List[Item]:
    results: List[Item] = []
    position: int = 0
    matched: bool = False
    for match in expression.expression.finditer(value):
        matched = True
        if position < match.start():
            results.append(Item(value[position:match.start()]))
        results.append(Item(value[match.start():match.end()], is_positive=expression.positive, is_token=True,
                            raise_level=expression.raise_level))
        position = match.end()
    if matched and position < len(value):
        results.append(Item(value[position:]))

    return results


def tokenize(item: Item) -> List[Item]:
    length: int = len(item.value)
    if item.is_token or length < 4:
        return [item]
    tokenized = []
    for expression in LOG_HIGHLIGHTS:
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
        complete += highlight(token.value, line.positive if token.is_positive else line.negative,
                              line.line) if token.is_token else token.value
    return complete


def process():
    try:
        while True:
            try:
                line: str = input()
                items: List[Item] = tokenize(Item(line))
                log_level: LogLevelRule = LOG_LEVELS[max(items, key=lambda item: item.raise_level).raise_level]
                print(highlight(join(items, log_level), log_level.line, ''))
            except EOFError:
                break
    except KeyboardInterrupt:
        sys.exit(0)
