import multiprocessing


def calcular(dado):
    return dado ** 2


def print_name_process():
    print(f"Starting the process: {multiprocessing.current_process().name}")

def main():
    size_pool = multiprocessing.cpu_count() * 2

    pools = multiprocessing.Pool(processes=size_pool, initializer=print_name_process)

    print(f"Size of pool: {size_pool}")

    inputs = list(range(7))
    outputs = pools.map(calcular, inputs)

    print(f"Outputs: {outputs}")

    pools.close()
    pools.join()


if __name__ == '__main__':
    main()
