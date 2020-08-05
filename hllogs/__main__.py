from typing import List


def generate_highlights():
    print("HIGHLIGHTS: List[str] = [")

    regexp_leading_highlights: List[str] = [

    ]

    full_word_highlights: List[str] = list(dict.fromkeys([
        'failed',
        'critical',
        'fatal',
        'error',
        'warning',
        'debug',
        'ready',
        'started',
        'starting',
        'connected',
        'disconnected',
        'installed',
        'installing',
        'disabled',
        'disabling',
        'closed',
        'dismounted',
        'stopping',
        'stopped',
        'shutdown',
        'completed',
        'exception',
        'successfully',
        'missing'
    ]))
    full_word_highlights.sort(key=len, reverse=True)

    regexp_trailing_highlights: List[str] = [
        r"ORA-\d+",  # oracle diagnostic messages
    ]

    for highlight in regexp_leading_highlights:
        print(" re.compile(r'{}'),".format(highlight))
    for highlight in full_word_highlights:
        print(" re.compile('{}', re.IGNORECASE),".format(highlight))
    for highlight in regexp_trailing_highlights:
        print(" re.compile(r'{}'),".format(highlight))
    print("]")


if __name__ == '__main__':
    generate_highlights()

# TODO fix empty lines breaking hllogs
# TODO comments
# TODO arguments
