import time
from concurrent.futures.thread import ThreadPoolExecutor as Executor
# from concurrent.futures.process import ProcessPoolExecutor as Executor

def processar():
    """
    # end para não pular linha ao imprimir.
    Flush para imprimir simultaneamente ao processamento
    """
    print('[', end='', flush=True)
    for i in range(1, 11):
        print(f' #-> {i}', end='', flush=True)
        time.sleep(1)
    print(' <- end]', end='', flush=True)
    return 42


if __name__ == '__main__':
    with Executor() as executor:
        future = executor.submit(processar)

    print(f'O retorno foi: {future.result()}')
