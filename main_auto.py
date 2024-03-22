import os
import requests
from datetime import datetime

def main():
    protocols = ['HTTP', 'SOCKS4', 'SOCKS5']
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")  # Get current timestamp
    output_directory = "./proxy/"
    os.makedirs(output_directory, exist_ok=True)  # Ensure the directory exists, create if not
    output_file = os.path.join(output_directory, f"proxy_{timestamp}.txt")  # Add timestamp to the output file name

    with open(output_file, 'w') as file:
        for protocol in protocols:
            website_url = f"https://yakumo.rei.my.id/{protocol}"
            prefix = protocol.lower()

            print(f"Fetching data for {protocol} protocol...")
            print(f"Website URL: {website_url}")
            print(f"Prefix: {prefix}")

            # Fetch the raw data from the website
            response = requests.get(website_url)

            if response.status_code == 200:
                raw_data = response.text.splitlines()
                print("Raw data fetched successfully:")
            else:
                print(f"Failed to fetch data from {website_url}. Status code: {response.status_code}")
                continue

            # Add the prefix before each IP address and write to the output file
            for ip in raw_data:
                file.write(f"{prefix}://{ip}\n")

            print("Data added successfully.\n")

if __name__ == "__main__":
    main()
