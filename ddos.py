#!/usr/bin/env python3
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

def send_request(url, timeout):
    """
    Belirtilen URL'ye GET isteği gönderir ve sonuç olarak durum kodunu döner.
    """
    try:
        response = requests.get(url, timeout=timeout)
        return f"{url} -> Status Code: {response.status_code}"
    except Exception as e:
        return f"{url} -> Error: {e}"

def main():
    # Kullanıcıdan giriş alıyoruz
    target_url = input("Hedef URL'yi girin: ")
    num_requests = int(input("Kaç istek göndermek istiyorsunuz? (Önerilen: 100): "))
    num_threads = int(input("Kaç thread kullanılsın? (Önerilen: 10): "))
    timeout = float(input("İstek zaman aşımı süresi (saniye)? (Önerilen: 5): "))

    print(f"\nHedef URL: {target_url}")
    print(f"Toplam {num_requests} istek, {num_threads} thread kullanılarak gönderilecek.\n")

    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        # Kullanıcıdan alınan bilgilere göre istekler oluşturuyoruz.
        futures = [executor.submit(send_request, target_url, timeout) for _ in range(num_requests)]

        # Görevler tamamlandıkça sonucu yazdırıyoruz.
        for future in as_completed(futures):
            print(future.result())

if __name__ == "__main__":
    main()
