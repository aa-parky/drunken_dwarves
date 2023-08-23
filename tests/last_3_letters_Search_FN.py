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

    with open(input_filename, 'r') as f:
        names = f.read().splitlines()

    last_three_letters = [extract_last_three_letters(name) for name in names if extract_last_three_letters(name)]

    freq_dist = Counter(last_three_letters)
    total_names = len(last_three_letters)

    sorted_freq_dist = sorted(freq_dist.items(), key=lambda x: x[1], reverse=True)

    user_search_term = input("Enter the last three letters to search: ").lower()
    matching_names = [name for name in names if extract_last_three_letters(name) == user_search_term]

    output_filename = f"first_name_ending_{user_search_term}.txt"

    with open(output_filename, 'w') as f_out:
        f_out.write(f"Matching First Names ending with '{user_search_term}':\n")
        for name in matching_names:
            f_out.write(name + '\n')

    print(f"Matching First Names ending with '{user_search_term}':")
    for name in matching_names:
        print(name)
