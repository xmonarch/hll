from typing import List


def generate_highlights():
    print("HIGHLIGHTS: List[str] = [")
    highlights: List[str] = list(dict.fromkeys([
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
        'disabled',
        'disabling',
        'closed',
        'dismounted',
        'stopping',
        'stopped',
        'shutdown',
        'completed',
        'exception'
    ]))
    regexp_highlights: List[str] = [
        r"ORA-\d+",  # oracle diagnostic messages
    ]
    highlights.sort(key=len, reverse=True)
    for highlight in highlights:
        print("'{}',".format(highlight))
    for highlight in regexp_highlights:
        print("'{}',".format(highlight))
    print("]")


if __name__ == '__main__':
    generate_highlights()
