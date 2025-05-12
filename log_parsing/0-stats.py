#!/usr/bin/python3
"""
Parses stdin log lines to compute file size and HTTP status code metrics.
"""
import sys

stats = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0
}
total_size = 0


def print_stats():
    print('File size: {}'.format(total_size))
    for s_code, count in sorted(stats.items()):
        if count:
            print('{}: {}'.format(s_code, count))


try:
    for i, line in enumerate(sys.stdin, start=1):
        matches = line.rstrip().split()
        try:
            status_code = matches[-2]
            file_size = matches[-1]
            if status_code in stats:
                stats[status_code] += 1
            total_size += int(file_size)
        except Exception:
            pass
        if i % 10 == 0:
            print_stats()
    print_stats()

except KeyboardInterrupt:
    print_stats()
    raise
