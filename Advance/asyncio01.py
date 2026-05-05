import asyncio

async def func():
    print("Start")
    await asyncio.sleep(2)  # Simulate an asynchronous operation
    print("End")

async def main():
    await asyncio.gather(
        func(), func(),func()
        )  # Run two instances of func concurrently

# Run the asynchronous function
asyncio.run(main())