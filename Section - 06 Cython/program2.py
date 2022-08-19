import datetime
import multiprocessing
import exercise_cython


def main():
    qtd_cores = multiprocessing.cpu_count()
    print(f"Carrying out the mathematical process with {qtd_cores} core(s)")

    start = datetime.datetime.now()

    exercise_cython.compute(end=50_000_000)

    time = datetime.datetime.now() - start
    print(f"Time: {time}")

    print(f"Finished in {time.total_seconds():.2f} seconds!")


if __name__ == '__main__':
    main()


"""
Em cython terminou em 10.68 segundos, sem funções!
Em cython terminou em 0.33 segundos com as funções em cython!
Em cython terminou em 0.28 segundos com as funções em cython e nogil!
Em cython terminou em 0.26 segundos com as funções em cython e nogil!
"""
