import os
import requests
from datetime import datetime
import time

# Variabel global untuk menghitung jumlah tugas yang sudah dikerjakan
total_tasks = 0

def main():
    global total_tasks  # Deklarasi variabel global total_tasks
    protocols = ['HTTP', 'SOCKS4', 'SOCKS5']
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")  # Mendapatkan timestamp saat ini
    output_directory = "./proxy/"
    os.makedirs(output_directory, exist_ok=True)  # Pastikan direktori ada, buat jika tidak
    output_file = os.path.join(output_directory, f"proxy_{timestamp}.txt")  # Tambahkan timestamp ke nama file output

    # Variabel untuk melacak tugas yang sebenarnya dihitung
    tasks_counted = 0

    with open(output_file, 'w') as file:
        for protocol in protocols:
            website_url = f"https://yakumo.rei.my.id/{protocol}"
            prefix = protocol.lower()

            print(f"Fetching data for {protocol} protocol...")
            print(f"Website URL: {website_url}")
            print(f"Prefix: {prefix}")

            # Fetch data mentah dari website
            response = requests.get(website_url)

            if response.status_code == 200:
                raw_data = response.text.splitlines()
                print("Raw data fetched successfully:")
            else:
                print(f"Failed to fetch data from {website_url}. Status code: {response.status_code}")
                continue

            # Menambahkan prefix sebelum setiap alamat IP dan menulis ke file output
            for ip in raw_data:
                file.write(f"{prefix}://{ip}\n")

            print("Data added successfully.\n")

            # Menginkrementasi jumlah tugas yang sebenarnya dihitung
            tasks_counted += 1

            # Jika sudah 3 tugas yang sebenarnya dihitung, tambahkan 1 ke total tugas dan reset hitung
            if tasks_counted == 3:
                total_tasks += 1
                tasks_counted = 0

    # Mencetak jumlah total tugas yang sudah dilakukan
    print(f"Total tasks completed: {total_tasks}")

    # Menunggu 10 detik sebelum menjalankan tugas lagi
    time.sleep(600)
    main()  # Memanggil fungsi main() secara rekursif setelah menunggu 10 detik

if __name__ == "__main__":
    main()
