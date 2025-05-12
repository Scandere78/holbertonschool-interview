import sys
import signal

def print_statistics(total_size, status_counts):
    print(f"File size: {total_size}")
    for code in sorted(status_counts.keys()):
        print(f"{code}: {status_counts[code]}")

def parse_line(line):
    parts = line.split()
    if len(parts) != 9:
        return None, None

    try:
        status_code = int(parts[-2])
        file_size = int(parts[-1])
    except ValueError:
        return None, None

    return status_code, file_size

def main():
    total_size = 0
    status_counts = {}
    line_count = 0

    def handle_interrupt(signum, frame):
        print_statistics(total_size, status_counts)
        sys.exit(0)

    signal.signal(signal.SIGINT, handle_interrupt)

    for line in sys.stdin:
        status_code, file_size = parse_line(line)
        if status_code is not None and file_size is not None:
            total_size += file_size
            status_counts[status_code] = status_counts.get(status_code, 0) + 1
            line_count += 1

            if line_count % 10 == 0:
                print_statistics(total_size, status_counts)

if __name__ == "__main__":
    main()
