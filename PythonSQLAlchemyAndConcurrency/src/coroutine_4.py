import asyncio
import time

async def me_first():
    await asyncio.sleep(1)

    return "I'm first!"

async def me_second():
    await asyncio.sleep(1)

    return "Then me!"

async def me_third():
    await asyncio.sleep(1)

    return "And finally me!"

async def main():
    start = time.perf_counter()

    first_result = await me_first()
    second_result = await me_second()
    third_result = await me_third()

    end = time.perf_counter()

    print(f"It took {end - start} seconds to complete all operations\n")

    print(first_result)
    print(second_result)
    print(third_result)


asyncio.run(main())