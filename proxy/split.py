def split_file(input_file, lines_per_file=2000):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    file_count = len(lines) // lines_per_file
    remainder = len(lines) % lines_per_file

    if remainder > 0:
        file_count += 1

    for i in range(file_count):
        start_idx = i * lines_per_file
        end_idx = start_idx + lines_per_file
        output_file = f"{input_file}_{i + 1}.txt"
        with open(output_file, 'w') as f:
            f.writelines(lines[start_idx:end_idx])

if __name__ == "__main__":
    input_file = input("Enter the name of the input file: ")
    lines_per_file = 2000  # Number of lines per file
    split_file(input_file, lines_per_file)
