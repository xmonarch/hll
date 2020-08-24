import argparse
import logging
import sys
from typing import List

from hll.ascii import Ascii
from hll.highlights import LOG_HIGHLIGHTERS, Highlighter
from hll.json import extract_json_attachments
from hll.levels import LOG_LEVELS, LogLevelRule
from hll.xml import extract_xml_attachments


class Token(object):
    """
    Objects representing a parsed on un-parsed token (literal)
    """

    """
    String value of the token
    """
    value: str

    """
    If True this token was not matched (yet?) to any highlighting rule
    """
    is_literal: bool

    """
    Log level requested by the token (by default logging.NOTSET is requested by literal tokens
    """
    raise_level: int

    """
    For highlighted token represents whether or not the token represents a positive or a negative information
    """
    positive: bool

    def __init__(self, value: str, is_literal: bool = True, raise_level: int = logging.NOTSET, positive: bool = False):
        self.value: str = value
        self.is_literal: bool = is_literal
        self.raise_level: int = raise_level
        self.positive: bool = positive


def highlight(value: str, escape: str, level_escapes: str) -> str:
    """
    Highlight a given token
    :param value: string contents of the token
    :param escape: ASCII escapes relevant to the token
    :param level_escapes: ASCII escapes relevant to the log level to resume after token
    :return: escaped string contents of the token
    """
    return f"{escape}{value}{Ascii.END}{level_escapes}"


def split(highlighter: Highlighter, value: str) -> List[Token]:
    """
    Split a given string into tokens for the given highlight pattern
    :param highlighter: highlighting object
    :param value: string contents of the literal to be split
    :return: a list of tokens as split by this highlighter, If the pattern is not matched and empty list is returned.
    """
    results: List[Token] = []
    position: int = 0
    matched: bool = False

    # find all tokens matching expression
    for match in highlighter.expression.finditer(value):
        matched = True
        if position < match.start():
            # append any trailing string contents as a literal token
            results.append(Token(value[position:match.start()]))

        # append the matched highlighted token with the details of the highlighter
        results.append(Token(value[match.start():match.end()], positive=highlighter.positive, is_literal=False,
                             raise_level=highlighter.raise_level))

        # register current position for the next iteration
        position = match.end()

    if matched and position < len(value):
        # append any left over string contents as a literal token
        results.append(Token(value[position:]))

    return results


def tokenize(item: Token, start_index: int = 0) -> List[Token]:
    """
    Turn a single literal token into a list by processing it with all registered highlighters.
    :param item: literal token
    :param start_index: index of the highlighter to start with
    :return: list of tokens in the order in which they should be joined with information needed for highlighting
    """
    length: int = len(item.value)
    if not item.is_literal or length < 4:
        # for non-literal or literals considered too short let's terminate here
        return [item]
    tokenized = []

    for index, highlighter in enumerate(LOG_HIGHLIGHTERS, start=start_index):
        # attempt to split with the given pattern
        parts = split(highlighter, item.value)

        # find the first applicable highlighter that splits the string
        if len(parts) > 0:
            # process all produced tokens
            for part in parts:
                if part.is_literal:
                    # literal tokens are processed further
                    tokenized.extend(tokenize(part, start_index=index + 1))
                else:
                    # recognized tokens are simply added to the list
                    tokenized.append(part)
            break

    return tokenized if len(tokenized) > 0 else [item]


def join(tokens: List[Token], line: LogLevelRule) -> str:
    """
    Join a list of tokens into a string. For the highlighted tokens the coloring is applied.
    :param tokens: list of parsed token
    :param line: recognized log level rule
    :return: a join list of contents of the tokens, with highlighted token being ASCII escaped accordingly
    """
    complete: str = ''
    for token in tokens:
        complete += highlight(token.value, line.positive if token.positive else line.negative,
                              line.line) if not token.is_literal else token.value
    return complete


def process():
    """
    Parse CLI arguments
    """
    parser = argparse.ArgumentParser(description="Colorize and highlight logs")
    parser.add_argument("-x",
                        "--no-xml",
                        dest="xml",
                        help="don't detect xml contents",
                        action="store_const",
                        default=True,
                        const=False)
    parser.add_argument("-j",
                        "--no-json",
                        dest="json",
                        help="don't detect json contents",
                        action="store_const",
                        default=True,
                        const=False)
    args = parser.parse_args(sys.argv[1:])

    """
    Process lines from input one by one and highlight configured phrases
    """
    try:
        while True:
            try:
                # read input
                line: str = input()

                # parse line into tokens
                items: List[Token] = tokenize(Token(line))

                # determine maximum log level and assigned coloring rule based on levels requested by recognized tokens
                log_level: LogLevelRule = LOG_LEVELS[max(items, key=lambda item: item.raise_level).raise_level]

                # colorize according to the level rule
                print(highlight(join(items, log_level), log_level.line, ''))

                if args.xml:
                    # extract XML attachments
                    for xml in extract_xml_attachments(line):
                        print(highlight(" > XML  ", Ascii.MAGENTA + Ascii.REVERSE + Ascii.BOLD, ''))
                        print(highlight(xml, Ascii.MAGENTA, ''))

                if args.json:
                    # extract JSON attachments
                    for xml in extract_json_attachments(line):
                        print(highlight(" > JSON ", Ascii.MAGENTA + Ascii.REVERSE + Ascii.BOLD, ''))
                        print(highlight(xml, Ascii.MAGENTA, ''))

            except EOFError:
                # once we run out of input we're done
                break
    except KeyboardInterrupt:
        # keyboard interrupt is perfectly fine
        sys.exit(0)
