import requests

def main():
    protocols = ['HTTP', 'SOCKS4', 'SOCKS5']

    for protocol in protocols:
        website_url = f"https://yakumo.rei.my.id/{protocol}"
        prefix = protocol.lower()
        output_file = f"{prefix}.txt"

        print(f"Fetching data for {protocol} protocol...")
        print(f"Website URL: {website_url}")
        print(f"Prefix: {prefix}")
        print(f"Output file: {output_file}")

        # Fetch the raw data from the website
        response = requests.get(website_url)

        if response.status_code == 200:
            raw_data = response.text.splitlines()
            print("Raw data fetched successfully:")
        else:
            print(f"Failed to fetch data from {website_url}. Status code: {response.status_code}")
            continue

        # Add the prefix before each IP address and write to a new file
        with open(output_file, 'w') as file:
            for ip in raw_data:
                file.write(f"{prefix}://{ip}\n")

        print("Prefix added successfully.\n")

if __name__ == "__main__":
    main()
