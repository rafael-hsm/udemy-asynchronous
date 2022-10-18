# 1 - Bibliotecas necessárias
## Comuns
import datetime
import math
from time import sleep

## Especifícas para multiprocessamento
import multiprocessing
from concurrent.futures.process import ProcessPoolExecutor


# 2 - Função para calcular raiz quadrada
def processamento(termina_em, inicia=1):
    pos = inicia
    fator = 1000 * 1000
    while pos < termina_em:
        pos += 1
        math.sqrt((pos - fator) * (pos - fator))


# 3 - Função sem multiprocesso
def sem_multiprocesso():
    hora_inicio = datetime.datetime.now()
    processamento(termina_em=10_000_000)
    tempo = datetime.datetime.now() - hora_inicio
    print(f"Terminou em {tempo.total_seconds():.2f} segundos sem multiprocessamento.")
    return tempo


# 4 - Função com multiprocesso
def com_multiprocesso():
    qtd_cores = multiprocessing.cpu_count()

    print(f'\nRealizanddo multiprocesso com {qtd_cores} cores.')
    start = datetime.datetime.now()

    with ProcessPoolExecutor(max_workers=qtd_cores) as executor:
        for n in range(1, qtd_cores + 1):
            inicio = 10_000_000 * (n - 1) / qtd_cores
            fim = 10_000_000 * n / qtd_cores
            print(f'Core {n} processando número {inicio} para numero {fim}')
            executor.submit(processamento, inicia=inicio, termina_em=fim)

    tempo_execucao = datetime.datetime.now() - start

    print(f'Com multiprocesso terminou em: {tempo_execucao.total_seconds():.2f} segundos!')

    return tempo_execucao


if __name__ == '__main__':
    x = sem_multiprocesso()
    y = com_multiprocesso()
    if y < x:
        print(f"Com multiprocesso foi aproximadamente {round(x/y, 2)}x mais rápido.")