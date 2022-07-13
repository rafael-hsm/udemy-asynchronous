import threading  # 1
import time


def main():
    th = threading.Thread(target=contar, args=('elefante', 10))  # 2
    th.start()  # add our thread in pool ready to run, but don't  # 3

    print('We can do others things as long as the thread keeps running.')
    print('==DEV - RHSM - DEV==\n' * 2)

    th.join()  # Warns to stay until thread finishes executing.  # 4

    print('Done')


def contar(o_que, numero):
    for n in range(1, numero + 1):
        print(f"{n} {o_que}(s)...")
        time.sleep(1)


if __name__ == '__main__':
    main()
