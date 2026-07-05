import asyncio
import aiohttp

URL = "http://127.0.0.1:8000"
ENDPOINTS = ["/items", "/items2", "/items3", "/items4"]
CONCURRENT_LIMIT = 100

async def send_request(session, semaphore, endpoint, value):
    async with semaphore:
        payload = {"name": value}
        try:
            async with session.post(f"{URL}{endpoint}", json=payload) as response:
                result = await response.json()
                print(f"✅ {endpoint} → {result}")
        except Exception as e:
            print(f"❌ {endpoint} → {e}")

async def load_test():
    semaphore = asyncio.Semaphore(CONCURRENT_LIMIT)
    async with aiohttp.ClientSession() as session:
        tasks = []
        for i in range(10):
           
            for endpoint in ENDPOINTS:
                tasks.append(send_request(session, semaphore, endpoint, f"test_{i}"))
        
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(load_test())