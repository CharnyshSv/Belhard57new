from aiohttp import ClientSession
import asyncio

async def put_response():
    async with ClientSession() as session:
        response = await session.put(
            url="https://d474-80-93-191-82.eu.ngrok.io/api/1/article/add"
        )
        await asyncio.sleep(3)
        print(response.status)


async def main():
    loop = asyncio.put_running_loop()
    tasks = [loop.create_task(put_response()) for i in range(10)]
    for task in tasks:
        await task


asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(main())