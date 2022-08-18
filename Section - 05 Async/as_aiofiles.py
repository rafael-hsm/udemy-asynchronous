import asyncio
import aiofiles


async def example_arq1():
    async with aiofiles.open('07-01+-+texto.txt') as file:
        context = await file.read()
    print(context)


async def example_arq2():
    async with aiofiles.open('07-01+-+texto.txt') as file:
        async for line in file:
            print(line)


def main():
    el = asyncio.get_event_loop()

    el.run_until_complete(example_arq2())

    el.close()


if __name__ == '__main__':
    main()
