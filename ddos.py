import aiohttp
import asyncio
import threading

async def fetch(session, url):
    try:
        async with session.get(url) as response:
            print(f"{url} - Status: {response.status}")
    except Exception as e:
        print(f"{url} - Error: {e}")

async def unlimited_requests(url, delay):
    async with aiohttp.ClientSession() as session:
        while True:
            await fetch(session, url)
            await asyncio.sleep(delay)  # Gecikme süresi

def start_async_loop(url, delay):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(unlimited_requests(url, delay))

# Kullanıcıdan giriş al
url = input("Lütfen URL'yi girin: ")
delay = float(input("İstekler arasındaki gecikmeyi (saniye) girin: "))
threads = int(input("Kaç adet iş parçacığı (thread) olsun?: "))

# Çoklu iş parçacıklı çalıştırma
for _ in range(threads):
    thread = threading.Thread(target=start_async_loop, args=(url, delay))
    thread.start()
