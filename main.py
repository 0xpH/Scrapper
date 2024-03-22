import requests

def main():
    print("Choose protocol:")
    print("1. HTTP")
    print("2. SOCKS4")
    print("3. SOCKS5")
    choice = input("Enter your choice (1/2/3): ")

    # Validate user choice
    if choice not in ['1', '2', '3']:
        print("Invalid choice. Exiting.")
        return

    website_url = ""
    prefix = ""
    output_file = ""

    if choice == '1':
        website_url = "https://yakumo.rei.my.id/HTTP"
        prefix = "http"
        output_file = "http.txt"
    elif choice == '2':
        website_url = "https://yakumo.rei.my.id/SOCKS4"
        prefix = "socks4"
        output_file = "socks4.txt"
    elif choice == '3':
        website_url = "https://yakumo.rei.my.id/SOCKS5"
        prefix = "socks5"
        output_file = "socks5.txt"

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
        return

    # Add the prefix before each IP address and write to a new file
    with open(output_file, 'w') as file:
        for ip in raw_data:
            file.write(f"{prefix}://{ip}\n")

    print("Prefix added successfully.")

if __name__ == "__main__":
    main()
