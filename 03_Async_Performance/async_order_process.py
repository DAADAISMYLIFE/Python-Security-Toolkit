import asyncio
import time
import random

async def cook_hamburger(n, t):
    print(f"start to cook {n} hamburger")
    await asyncio.sleep(t)
    print(f"completed {n} hamburger")


async def cook_coke(n, t):
    print(f"start to cook {n} coke")
    await asyncio.sleep(t)
    print(f"completed {n} coke")


async def cook_fries(n, t):
    print(f"start to cook {n} fries")
    await asyncio.sleep(t)
    print(f"completed {n} fries")

async def order(n):
    print(f"start the customer {n}'s order ")
    tasks = [
        asyncio.create_task(cook_hamburger(n, random.random())),
        asyncio.create_task(cook_coke(n, random.random())),
        asyncio.create_task(cook_fries(n, random.random()))
    ]

    await asyncio.gather(*tasks)
    print(f"--- finish the {n}'s order ---")


async def main():
    customer_count = int(input("number of customers: "))
    tasks = []
    for i in range(customer_count):
        task = asyncio.create_task(order(i + 1))
        tasks.append(task)

    await asyncio.gather(*tasks)
    

if __name__ == '__main__':
    asyncio.run(main())