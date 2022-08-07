# from requests import Session
# from time import sleep
#
# def get_response():
#     with Session() as session:
#         response = session.get(
#             url="https://developerhub.alfabank.by:8273/partner/1.0.1/public/rates"
#         )
#         print(response.json())
#         print(response.text)
#         print(response.cookies)
#         print(response.headers)
#         print(response.url)
#         print(response.status_code)
#
# for i in range(10):
#     get_response()

from aiohttp import ClientSession
import asyncio

async def get_response():
    async with ClientSession() as session:
        response = await session.get(
            url="https://developerhub.alfabank.by:8273/partner/1.0.1/public/rates"
        )
        await asyncio.sleep(3)
        print(response.status)
async def main():
    loop = asyncio.get_running_loop()
    tasks = [loop.create_task(get_response()) for i in range(10)]
    for task in tasks:
        await task
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(main())
