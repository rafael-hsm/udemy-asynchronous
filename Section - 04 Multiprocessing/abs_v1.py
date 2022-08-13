import threading
import time


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


if __name__ == '__main__':
    ex = threading.Thread(target=processar)

    ex.start()
    ex.join()
