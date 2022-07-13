import threading  # 1
import time


def main():
    threads = [
        threading.Thread(target=count, args=('elephant', 10)),  # 2
        threading.Thread(target=count, args=('hole', 8)),
        threading.Thread(target=count, args=('coin', 23)),
        threading.Thread(target=count, args=('duck', 12)),
               ]
    [th.start() for th in threads]  # add our thread in pool ready to run, but don't  # 3

    print('We can do others things as long as the thread keeps running.')
    print('==DEV - RHSM - DEV==\n' * 2)

    [th.join() for th in threads]  # Warns to stay until thread finishes executing.  # 4

    print('Done')


def count(what, number):
    for n in range(1, number + 1):
        print(f"{n} {what}(s)...")
        time.sleep(1)


if __name__ == '__main__':
    main()
