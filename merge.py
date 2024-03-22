import os
import datetime

def merge_text_files():
    try:
        # Create directory if it doesn't exist
        output_directory = 'proxy'
        os.makedirs(output_directory, exist_ok=True)
        
        # Generate output file name based on current timestamp
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        output_file = os.path.join(output_directory, f"proxy_{timestamp}.txt")

        with open(output_file, 'w') as out_f:
            # Get all .txt files in the current directory
            txt_files = [file for file in os.listdir() if file.endswith('.txt')]
            for file_name in txt_files:
                with open(file_name, 'r') as in_f:
                    out_f.write(in_f.read())
        print("Merging successful.")
        return output_file
    except Exception as e:
        print(f"Error occurred: {str(e)}")
        return None

# Example usage:
merged_file = merge_text_files()
if merged_file:
    print(f"Merged file created: {merged_file}")
else:
    print("Merging failed.")
