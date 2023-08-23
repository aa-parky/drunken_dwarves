def main():
    input_file_name = "all_JJ.txt"
    output_file_name = "modified_JJ.txt"

    try:
        with open(input_file_name, 'r') as input_file:
            lines = input_file.readlines()

        modified_lines = []
        for line in lines:
            if "_" in line:
                modified_line = line.replace('_', '-')
                modified_lines.append(modified_line)
            elif not any(char.isdigit() for char in line):
                modified_lines.append(line)

        with open(output_file_name, 'w') as output_file:
            output_file.writelines(modified_lines)

        print("Modification and filtering successful. Modified content saved to", output_file_name)

    except FileNotFoundError:
        print("Input file not found:", input_file_name)
    except Exception as e:
        print("An error occurred:", str(e))


if __name__ == "__main__":
    main()
