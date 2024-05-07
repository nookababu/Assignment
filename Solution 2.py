import asyncio
import aiohttp
async def fetch_url(session, url, semaphore):
    async with semaphore:
        try:
            async with session.get(url) as response:
                content = await response.text()
                print(f"Downloaded content from {url}: {content}")
        except aiohttp.ClientError:
            print(f"Failed to download content from {url}")

async def download_urls(urls):
    semaphore = asyncio.Semaphore(5)
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url, semaphore) for url in urls]
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    urls = [
        "https://example.com",
        "https://example.org",
        "https://example.net"
    ]
    asyncio.run(download_urls(urls))