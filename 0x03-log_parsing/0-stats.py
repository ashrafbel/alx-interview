#!/usr/bin/python3
"Log parsing"
import sys
import signal


totalSize = 0
status_codes_count = {
    "200": 0, "301": 0, "400": 0, "401": 0,
    "403": 0, "404": 0, "405": 0, "500": 0
}
contLine = 0


def print_stats():
    """Print the computed statistics"""
    print(f"File size: {totalSize}")
    for code in sorted(status_codes_count.keys()):
        if status_codes_count[code] > 0:
            print(f"{code}: {status_codes_count[code]}")


def signal_handler(sig, frame):
    """Handle keyboard interruption (CTRL + C)"""
    print_stats()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)
for line in sys.stdin:
    line = line.strip()
    try:
        parts = line.split()
        if len(parts) < 7:
            continue
        status_code = parts[-2]
        file_size = int(parts[-1])
        totalSize += file_size
        if status_code in status_codes_count:
            status_codes_count[status_code] += 1
        contLine += 1
        if contLine % 10 == 0:
            print_stats()
    except Exception:
        continue
print_stats()
