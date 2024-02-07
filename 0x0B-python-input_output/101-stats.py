#!/usr/bin/python3
"""standard input and computes metrics
"""


def print_stats(size, status_codes):
    """accumulated metrics
    """
    print("File size: {}".format(size))
    for key in sorted(status_codes):
        print("{}: {}".format(key, status_codes[key]))


if __name__ == "__main__":
    import sys

    s = 0
    status_codes = {}
    valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    c = 0

    try:
        for line in sys.stdin:
            if c == 10:
                print_stats(s, status_codes)
                c = 1
            else:
                c += 1

            line = line.split()

            try:
                s += int(line[-1])
            except (IndexError, ValueError):
                pass

            try:
                if line[-2] in valid_codes:
                    if status_codes.get(line[-2], -1) == -1:
                        status_codes[line[-2]] = 1
                    else:
                        status_codes[line[-2]] += 1
            except IndexError:
                pass

        print_stats(s, status_codes)

    except KeyboardInterrupt:
        print_stats(s, status_codes)
        raise
