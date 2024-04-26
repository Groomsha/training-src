from typing import List
import time

import asyncio


async def task_one() -> None:
    number: int = 1

    while True:
        print(f'Task One: Print Number - {number}')
        number += 1
        await asyncio.sleep(1)


async def task_two() -> None:
    while True:
        print(f'Task Two: Print Time - {time.time()}')
        await asyncio.sleep(1)


async def as_main() -> None:
    tasks: List = list()

    tasks.append(asyncio.create_task(task_two()))
    tasks.append(asyncio.create_task(task_one()))

    await asyncio.gather(*tasks)


if __name__ == '__main__':
    asyncio.run(as_main())
