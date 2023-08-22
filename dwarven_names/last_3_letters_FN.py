from collections import Counter

def extract_last_three_letters(name):
    parts = name.split()
    if len(parts) >= 3 and parts[1] == 'the':
        first_name = parts[0]
        last_three_letters = first_name[-3:]
        return last_three_letters
    else:
        return None  # Or handle the case differently based on your requirements

if __name__ == "__main__":
    input_filename = "input.txt"
    output_filename = "output.txt"

    with open(input_filename, 'r') as f:
        names = f.read().splitlines()

    last_three_letters = [extract_last_three_letters(name) for name in names if extract_last_three_letters(name)]

    freq_dist = Counter(last_three_letters)
    total_names = len(last_three_letters)

    sorted_freq_dist = sorted(freq_dist.items(), key=lambda x: x[1], reverse=True)

    with open(output_filename, 'w') as f_out:
        f_out.write("Last Three Letters Frequency:\n")
        for letters, frequency in sorted_freq_dist:
            percentage = (frequency / total_names) * 100
            f_out.write(f"{letters}: {frequency} ({percentage:.2f}%)\n")

    print("Last Three Letters Frequency:")
    for letters, frequency in sorted_freq_dist:
        percentage = (frequency / total_names) * 100
        print(f"{letters}: {frequency} ({percentage:.2f}%)")
