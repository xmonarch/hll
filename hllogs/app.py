import sys


def highlight():
    try:
        while True:
            try:
                line = input()
                print('The line is:"%s"' % line)
            except EOFError:
                break
    except KeyboardInterrupt:
        sys.exit(0)
