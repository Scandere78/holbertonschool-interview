#!/usr/bin/python3
"""
Parses logs from stdin and computes statistics:
- total file size
- count of status codes
"""

import sys
import re
from collections import defaultdict

total_size = 0
status_counts = defaultdict(int)
valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
line_count = 0

def print_stats():
    print(f"File size: {total_size}")
    for code in sorted(status_counts):
        if code in valid_codes:
            print(f"{code}: {status_counts[code]}")

try:
    for line in sys.stdin:
        match = re.fullmatch(
            r'[\d.]+ - \[.*\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)\n?', line)
        if match:
            code, size = match.groups()
            total_size += int(size)
            if code in valid_codes:
                status_counts[code] += 1
            line_count += 1

            if line_count % 10 == 0:
                print_stats()

except KeyboardInterrupt:
    print_stats()
    raise

print_stats()
