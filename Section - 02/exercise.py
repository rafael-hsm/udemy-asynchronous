import datetime
import math


def main():
    start = datetime.datetime.now()

    compute(end=50_000_000)

    time = datetime.datetime.now() - start

    print(f"Finished in {time.total_seconds():.2f} segundos.")


def compute(end, start=1):
    pos = start
    factor = 1000 * 1000
    while pos < end:
        pos += 1
        math.sqrt((pos - factor) * (pos - factor))


if __name__ == '__main__':
    main()

"""
Terminou em 33.60 segundos.
"""

