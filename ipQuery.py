# IP Sorgu Aracına Hoş Geldiniz... #
import requests
import time
import os

# Giriş Paneli
print("Github: ZCTools")
print("Instagram: zer0crypt0")
print("----------------")
print("---- WELCOME ---")
print("----------------")
time.sleep(2)
os.system("clear")
# Sorgu Bölümü
def get_ip_info(target_IP_Address):
    url = f'https://ipapi.co/{target_IP_Address}/json/'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return "IP bilgisi alınamadı. Hata kodu: " + str(response.status_code)

def main():
    target_IP_Address = input("Lütfen bir IP adresi girin: ")
    info = get_ip_info(target_IP_Address)
    if isinstance(info, dict):
        city = info.get('Şehir: ', 'Bilgi yok') # Şehir
        country = info.get('Ülke: ', 'Bilgi yok') # Ülke
        state = info.get('Eyalet: ', 'Bilgi yok') # Eyalet
        org = info.get('Kuruluş: ', 'Bilgi yok')
        print(f"IP Adresi: {target_IP_Address}\n[+] Ülke: {country}")
        print(f"[+] Şehir: {city}")
        print(f"[+] Eyalet: {state}")
        print(f"[+] Kuruluş: {org}")
    else:
        print(info)

if __name__ == "__main__":
    main()
