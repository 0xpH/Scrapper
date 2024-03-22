import requests
import sys

def main():
    if len(sys.argv) != 4:
        print("Usage: python main.py website_url prefix output_file")
        return

    website_url = sys.argv[1]
    prefix = sys.argv[2]
    output_file = sys.argv[3]

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
