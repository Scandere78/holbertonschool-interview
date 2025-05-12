#!/usr/bin/python3
import sys
import re
from collections import defaultdict

# Regex pour le format attendu
pattern = re.compile(
    r'^\d{1,3}(\.\d{1,3}){3} - \[.*?\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)$'
)

status_codes = defaultdict(int)
total_size = 0
line_count = 0
valid_status = ['200', '301', '400', '401', '403', '404', '405', '500']


def print_stats():
    print("File size: {}".format(total_size))
    for code in sorted(valid_status):
        if status_codes[code]:
            print("{}: {}".format(code, status_codes[code]))


try:
    for line in sys.stdin:
        match = pattern.match(line.strip())
        if match:
            status, size = match.group(2), match.group(3)
            total_size += int(size)
            if status in valid_status:
                status_codes[status] += 1
            line_count += 1

            if line_count == 10:
                print_stats()
                line_count = 0
except KeyboardInterrupt:
    print_stats()
    raise
else:
    print_stats()
