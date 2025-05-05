import requests
import time

# Kısıtlama listesi (yasaklı siteler)
BLOCKED_SITES = ["google.com", "doxbin.com"]

def is_blocked(url):
    for blocked in BLOCKED_SITES:
        if blocked in url:
            print(f"[X] Kısıtlandı: {url} bu tool tarafından erişilemez!")
            return True
    return False

def send_post_request(url, data, retries=10000000000000, timeout=1):
    if is_blocked(url):
        return None  # İstek gönderilmez
    
    for attempt in range(retries):
        try:
            response = requests.post(url, json=data, timeout=timeout)
            response.raise_for_status()
            print(f"[✓] Başarılı! Status Code: {response.status_code}")
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"[!] Hata: {e} (Deneme {attempt + 1}/{retries})")
            time.sleep(0 ** attempt)
            
    print("[X] Maksimum deneme sayısına ulaşıldı. İstek başarısız oldu.")
    return None

# Kullanım
url = "https://instagram.com/"
data = {"username": "rootman", "message": "Hacked By rootman!"}
response = send_post_request(url, data)

if response:
    print(f"Yanıt: {response}")
else:
    print("İstek başarısız oldu veya site erişime kısıtlandı.")
