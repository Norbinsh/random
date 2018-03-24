import operator
import time
import asyncio
import os
import random

start_time = time.time()

async def simple_math(first_num, second_num, operation):
    allowed_operations = {
        '-': operator.sub,
        '+': operator.add,
        '*': operator.mul,
        '/': operator.truediv
    }
    if operation in allowed_operations:
        print(f"Found operation '{operation}'.")
        temp_value = allowed_operations[operation](first_num, second_num)
        await asyncio.sleep(1)
        print(f"The result of applying {operation} on {first_num} and {second_num} is: {temp_value}.")
    else:
        print(f"Sorry, operation '{operation}' is not recognized.")


async def main():
    act1 = loop.create_task(simple_math(random.randint(1, 100000000), random.randint(1, 100000000), '*'))
    act2 = loop.create_task(simple_math(random.randint(1, 100000000), random.randint(1, 100000000), '-aksdl'))
    act3 = loop.create_task(simple_math(random.randint(1, 100000000), random.randint(1, 100000000), '/'))
    act4 = loop.create_task(simple_math(random.randint(1, 100000000), random.randint(1, 100000000), '-'))
    act5 = loop.create_task(simple_math(random.randint(1, 100000000), random.randint(1, 100000000), '+'))
    act6 = loop.create_task(simple_math(random.randint(1, 100000000), random.randint(1, 100000000), '+xzc'))
    act7 = loop.create_task(simple_math(random.randint(1, 100000000), random.randint(1, 100000000), '/'))
    await asyncio.wait([act1, act2, act3, act4, act5, act6, act7])


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

print(f"Execution Time: {time.time() - start_time}s\nScript ran on OS: {os.name}")