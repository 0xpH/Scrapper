import os
import datetime

def merge_text_files(input_files):
    try:
        # Create directory if it doesn't exist
        output_directory = 'proxy'
        os.makedirs(output_directory, exist_ok=True)
        
        # Generate output file name based on current timestamp
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        output_file = os.path.join(output_directory, f"proxy_{timestamp}.txt")

        with open(output_file, 'w') as out_f:
            for file_name in input_files:
                with open(file_name, 'r') as in_f:
                    out_f.write(in_f.read())
        print("Merging successful.")
        return output_file
    except Exception as e:
        print(f"Error occurred: {str(e)}")
        return None

# Example usage:
input_files = ['socks4.txt', 'socks5.txt', 'http.txt']
merged_file = merge_text_files(input_files)
if merged_file:
    print(f"Merged file created: {merged_file}")
else:
    print("Merging failed.")
