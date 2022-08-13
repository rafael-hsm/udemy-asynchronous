import multiprocessing

print(f"Starting the process with name: {multiprocessing.current_process().name}")


def make_something(value):
    print(f"Making something with the {value}")


def main():
    pc = multiprocessing.Process(target=make_something, args=('Bird',))

    print(f"Starting the process with name: {pc.name}")

    pc.start()
    pc.join()


if __name__ == '__main__':
    main()
