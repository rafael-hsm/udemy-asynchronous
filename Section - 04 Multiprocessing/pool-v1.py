import multiprocessing


def calcular(dado):
    return dado ** 2


def main():
    size_pool = multiprocessing.cpu_count() * 2

    pools = multiprocessing.Pool(processes=size_pool)

    print(f"Size of pool: {size_pool}")

    inputs = list(range(70))
    outputs = pools.map(calcular, inputs)

    print(f"Outputs: {outputs}")

    pools.close()
    pools.join()


if __name__ == '__main__':
    main()
