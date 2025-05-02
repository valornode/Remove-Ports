def remove_colon_and_beyond(input_file, output_file):
    """Removes ':' and anything after it on each line of the input file."""
    try:
        with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
            for line in infile:
                modified_line = line.split(':', 1)[0].strip()
                outfile.write(modified_line + '\n')
        print(f"Processed lines saved to '{output_file}'.")
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    input_file = "input.txt"
    output_file = "output.txt"
    remove_colon_and_beyond(input_file, output_file)
