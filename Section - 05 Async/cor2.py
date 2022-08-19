import asyncio


async def oi_demorado():
    print("Oi...")
    await asyncio.sleep(2)
    print("todos...")


# el = asyncio.get_event_loop()
# el.run_until_complete(oi_demorado())

asyncio.run(oi_demorado())
