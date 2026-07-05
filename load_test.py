import asyncio
import aiohttp
import time

URL = "http://127.0.0.1:8000"
ENDPOINTS = ["/items", "/items2", "/items3", "/items4"]
CONCURRENT_LIMIT = 200
TOTAL_REQUESTS = 2000

# Statistics counters
success_count = 0
failure_count = 0

async def send_request(session, semaphore, endpoint, value):
    global success_count, failure_count
    async with semaphore:
        payload = {"name": value}
        try:
            async with session.post(f"{URL}{endpoint}", json=payload) as response:
                if response.status == 200:
                    success_count += 1
                else:
                    failure_count += 1
        except Exception:
            failure_count += 1

async def load_test():
    global success_count, failure_count
    success_count = 0
    failure_count = 0

    semaphore = asyncio.Semaphore(CONCURRENT_LIMIT)
    
    print(f"🚀 Starting load test...")
    print(f"🔗 Target: {URL}")
    print(f"📊 Total planned requests: {TOTAL_REQUESTS}")
    print(f"⚡ Concurrency limit: {CONCURRENT_LIMIT}")
    
    start_time = time.perf_counter()
    
    async with aiohttp.ClientSession() as session:
        tasks = []
        for i in range(TOTAL_REQUESTS):
            endpoint = ENDPOINTS[i % len(ENDPOINTS)]
            tasks.append(send_request(session, semaphore, endpoint, f"load_test_{i}"))
        
        await asyncio.gather(*tasks)
        
    end_time = time.perf_counter()
    duration = end_time - start_time
    total_completed = success_count + failure_count
    tps = total_completed / duration if duration > 0 else 0
    
    print("\n================ STATS SUMMARY ================")
    print(f"⏱️  Total Duration: {duration:.2f} seconds")
    print(f"✅ Successes: {success_count}")
    print(f"❌ Failures: {failure_count}")
    print(f"📈 Throughput: {tps:.2f} requests/sec")
    print("===============================================")

if __name__ == "__main__":
    asyncio.run(load_test())