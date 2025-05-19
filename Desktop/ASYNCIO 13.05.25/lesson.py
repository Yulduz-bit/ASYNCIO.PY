import asyncio
import time

async def task1():
    print("start1")
    await asyncio.sleep(3)
    print("end1")

async def task2():
    print("task")
    await asyncio.sleep(2)
    print("end2")

async def task3():
    print("task3")
    await asyncio.sleep(1)
    print("end3")

async def main():
    started = time.time()
    await asyncio.gather(
        task1(),
        task2(),
        task3()
    )
    end = time.time()
    print(f"total time: {end - started:} seconds")

asyncio.run(main())

# async def func1()
#     print("start1")
#     await asyncio.sleep(1)
#     print("end")
# async def task2():
#     print("start2")
#     await asyncio.sleep(1)
#     print("end2")
#
# async def main():
#     await asyncio.gather(func1(), task2())
#
#     asyncio.run(main())
