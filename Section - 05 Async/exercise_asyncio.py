import datetime
import math
import asyncio


def main():
    print(f'Realizando o processamento matemático de forma assíncrona.')

    el = asyncio.get_event_loop()

    inicio = datetime.datetime.now()

    # el.run_until_complete(computar(inicio=1, fim=50_000_000))

    task1 = el.create_task(computar(inicio=1, fim=10_000_000))
    task2 = el.create_task(computar(inicio=10_000_001, fim=20_000_000))
    task3 = el.create_task(computar(inicio=20_000_001, fim=30_000_000))
    task4 = el.create_task(computar(inicio=30_000_001, fim=40_000_000))
    task5 = el.create_task(computar(inicio=40_000_001, fim=50_000_000))

    tasks = asyncio.gather(task1, task2, task3, task4, task5)

    el.run_until_complete(tasks)

    tempo = datetime.datetime.now() - inicio
    print(f'Terminou em {tempo.total_seconds():.2f} segundos.')


async def computar(fim, inicio=1):
    pos = inicio
    fator = 1000 * 1000
    while pos < fim:
        pos += 1
        math.sqrt((pos - fator) * (pos - fator))


if __name__ == '__main__':
    main()


"""
Terminou em 33.60 segundos.
Terminou em 13.11 segundos. Desktop
"""

"""
Using thread 
Finished in 25.62 seconds. Laptop
Finished in 23.62 seconds. Desktop
"""

"""
Using multiprocessing 
Finished in 18.81 seconds. Laptop
Finished in 2.56 seconds. Desktop
"""

"""
Using asyncio
Finished in 13.75 segundos. Desktop versão 1
Finished in 13.40 segundos. Desktop versão 2
"""
