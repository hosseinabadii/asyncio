import asyncio
import logging
import random
import time


async def func(x: int, y: int) -> int:
    logging.info(f"Calling func with {x=} and {y=}")
    random_time = random.randint(1, 3)
    logging.info(f"Waiting for {random_time} seconds")
    # if random_time == 2:
    #     raise Exception("Some error")
    await asyncio.sleep(random_time)
    return x + y


async def main():
    task1 = asyncio.create_task(func(10, 20))
    task2 = asyncio.create_task(func(11, 22))
    task3 = asyncio.create_task(func(33, 44))
    tasks = [task1, task2, task3]
    results = await asyncio.gather(*tasks)

    # async with asyncio.TaskGroup() as tg:
    #     task1 = tg.create_task(func(10, 20))
    #     task2 = tg.create_task(func(11, 22))
    #     task3 = tg.create_task(func(33, 44))
    #     tasks = [task1, task2, task3]
    # results = [task.result() for task in tasks]

    print(*results, sep="\n")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    start_time = time.perf_counter()
    asyncio.run(main())
    duration = time.perf_counter() - start_time
    logging.info(f"Tasks completed in {duration:.2f} seconds")
