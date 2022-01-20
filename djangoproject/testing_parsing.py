import aiohttp
import asyncio


async def fetch(session, url):
    async with session.get(url) as response:
        if response.status != 200:
            response.raise_for_status()
        return await response.text()


async def fetch_all(session, urls):
    tasks = []
    for url in urls:
        task = asyncio.create_task(fetch(session, url))
        tasks.append(task)
    results = await asyncio.gather(*tasks)
    return results


async def main():
    urls = ['http://0.0.0.0:8080/1/',
            'http://0.0.0.0:8080/2/',
            'http://0.0.0.0:8080/3/']

    async with aiohttp.ClientSession() as session:
        htmls = await fetch_all(session, urls)
        print(htmls)

        with open('content.txt', 'w') as the_file:
            the_file.write(str(htmls))


if __name__ == '__main__':
    asyncio.run(main())
