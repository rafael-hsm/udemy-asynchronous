import datetime
import asyncio


async def generate_data(quantity: int, data: asyncio.Queue):
    print(f'Wait the generation of {quantity} data...')
    for idx in range(1, quantity + 1):
        item = idx * idx
        await data.put((item, datetime.datetime.now()))
        await asyncio.sleep(0.001)
    print(f'{quantity} successfully generated data')


async def processing_data(quantity: int, data: asyncio.Queue):
    print(f'Wait the processing of {quantity} data ...')
    processing = 0
    while processing < quantity:
        await data.get()
        processing += 1
        await asyncio.sleep(0.001)
    print(f'{processing} items were processed.')


def main():
    total = 1_000
    data = asyncio.Queue()
    print(f'Computing {total * 2:.2f} data.')

    el = asyncio.get_event_loop()
    task1 = el.create_task(generate_data(total, data))
    task2 = el.create_task(generate_data(total, data))
    task3 = el.create_task(processing_data(total * 2, data))

    tasks = asyncio.gather(task1, task2, task3)

    el.run_until_complete(tasks)

    el.close()


if __name__ == '__main__':
    main()
