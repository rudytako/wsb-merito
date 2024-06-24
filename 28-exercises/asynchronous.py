import asyncio

'''Write a Python program that creates an asynchronous function to print 
"Python Exercises!" with a two second delay.'''
async def print_message():
    await asyncio.sleep(2)
    print("Python Exercises!")

'''Write a Python program that creates three asynchronous functions and displays
their respective names with different delays (1 second, 2 seconds, and 3 seconds).'''
async def func1():
    await asyncio.sleep(1)
    print("Function 1 executed")

async def func2():
    await asyncio.sleep(2)
    print("Function 2 executed")

async def func3():
    await asyncio.sleep(3)
    print("Function 3 executed")

async def main():
    await asyncio.gather(func1(), func2(), func3())

'''Write a Python program that creates an asyncio event loop and runs a coroutine that 
prints numbers from 1 to 7 with a delay of 1 second each.'''
async def print_numbers():
    for i in range(1, 8):
        print(i)
        await asyncio.sleep(1)

'''Write a Python program that implements a coroutine to fetch data from two 
different URLs simultaneously using the "aiohttp" library.'''
import aiohttp

async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def main():
    url1 = 'http://example.com'
    url2 = 'http://example.org'
    
    task1 = asyncio.create_task(fetch(url1))
    task2 = asyncio.create_task(fetch(url2))
    
    response1 = await task1
    response2 = await task2
    
    print(response1[:100])
    print(response2[:100])

'''Write a Python program that runs multiple asynchronous tasks concurrently 
using asyncio.gather() and measures the time taken.'''
import time

async def task1():
    await asyncio.sleep(1)
    return "Task 1 completed"

async def task2():
    await asyncio.sleep(2)
    return "Task 2 completed"

async def task3():
    await asyncio.sleep(3)
    return "Task 3 completed"

async def main():
    start_time = time.time()
    
    results = await asyncio.gather(task1(), task2(), task3())
    
    for result in results:
        print(result)
    
    end_time = time.time()
    print(f"Total time taken: {end_time - start_time} seconds")

'''Write a Python program to create a coroutine that simulates a time-consuming 
task and use asyncio.CancelledError to handle task cancellation.'''
async def long_running_task():
    try:
        print("Task started")
        await asyncio.sleep(10)
        print("Task completed")
    except asyncio.CancelledError:
        print("Task was cancelled")

async def main():
    task = asyncio.create_task(long_running_task())
    
    await asyncio.sleep(2)
    task.cancel()
    
    try:
        await task
    except asyncio.CancelledError:
        print("Handled task cancellation")


'''Write a Python program that implements a timeout for an asynchronous operation using asyncio.wait_for().'''
async def long_running_task():
    await asyncio.sleep(5)
    return "Task completed"

async def main():
    try:
        result = await asyncio.wait_for(long_running_task(), timeout=2)
        print(result)
    except asyncio.TimeoutError:
        print("Task timed out")


'''Write a Python program that uses asyncio queues to simulate a producer-consumer 
scenario with multiple producers and a single consumer.'''
import random

async def producer(queue, n):
    for i in range(n):
        item = random.randint(1, 100)
        await queue.put(item)
        print(f"Produced {item}")
        await asyncio.sleep(random.random())

async def consumer(queue):
    while True:
        item = await queue.get()
        if item is None:
            break
        print(f"Consumed {item}")
        await asyncio.sleep(random.random())

async def main():
    queue = asyncio.Queue()

    producers = [asyncio.create_task(producer(queue, 5)) for _ in range(3)]
    consumer_task = asyncio.create_task(consumer(queue))
    
    await asyncio.gather(*producers)
    await queue.put(None)
    await consumer_task

asyncio.run(main())
