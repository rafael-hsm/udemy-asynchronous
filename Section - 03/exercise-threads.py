import datetime
import math

import threading
import multiprocessing


def main():
    qtd_cores = multiprocessing.cpu_count()
    print(f"Carrying out the mathematical process with {qtd_cores} core(s)")

    start = datetime.datetime.now()

    threads = []
    for n in range(1, qtd_cores + 1):
        init = 50_000_000 * (n - 1) / qtd_cores
        end = 50_000_000 * n / qtd_cores
        print(f"Core {n} processing from number {init} to number {end}!")
        threads.append(
            threading.Thread(
                target=compute,
                kwargs={'start': init, 'end': end},
                daemon=True
            )
        )

    [th.start() for th in threads]
    [th.join() for th in threads]

    time = datetime.datetime.now() - start
    print(f"Time: {time}")

    print(f"Finished in {time.total_seconds():.2f} seconds!")


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

"""
Using thread 
Finished in 25.62 seconds. Laptop
Finished in 23.62 seconds. Desktop
"""