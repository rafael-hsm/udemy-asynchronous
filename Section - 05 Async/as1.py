import datetime
import asyncio


async def data_generator(quantity: int, data: asyncio.Queue):
    print(f"Wait the generation of {quantity} data...")
    for idx in range(1, quantity + 1):
        item = idx * idx
        await data.put((item, datetime.datetime.now()))
        await asyncio.sleep(0.001)

    print(f'{quantity} successfully generated data...')


async def processing_data(quantity: int, data: asyncio.Queue):
    print(f'Wait the processing of {quantity} data ...')
    processing = 0
    while processing < quantity:
        await data.get()
        processing += 1
        await asyncio.sleep(0.001)
    print(f'Processed {processing} items')


if __name__ == '__main__':
    total = 5_000
    dados = asyncio.Queue()
    el = asyncio.get_event_loop()

    print(f'Computing {total * 2:.2f} data.')

    el.run_until_complete(data_generator(total, dados))
    el.run_until_complete(data_generator(total, dados))
    el.run_until_complete(processing_data(total * 2, dados))

    el.close()
