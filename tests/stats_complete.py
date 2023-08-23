import re
from nltk import FreqDist
from collections import Counter

def calculate_percentage(repeated_count, total_count):
    return (repeated_count / total_count) * 100

def write_to_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)

# Read the input.txt file
with open('input.txt', 'r') as file:
    text = file.read()

# Extract first names using regular expressions
first_names = re.findall(r'\b\w+\b the', text)
first_names = [name[:-4] for name in first_names]
first_name_freq = FreqDist(first_names)

# Extract last names using regular expressions
last_names = re.findall(r'the (\w+)', text)
last_name_freq = FreqDist(last_names)

# Find exact duplicate lines
lines = text.splitlines()
line_counter = Counter(lines)
duplicate_line_numbers = {line: [i + 1 for i, l in enumerate(lines) if l == line] for line, count in
                          line_counter.items() if count > 1}

# Initialize variables for name and line totals
total_first_names = len(first_names)
total_repeated_first_names = 0
total_last_names = len(last_names)
total_repeated_last_names = 0

# Prepare strings to hold the name and line results
first_name_output = ""
last_name_output = ""
duplicate_line_output = ""

# Display and add first names occurring more than 1 time to the output string
for name, freq in first_name_freq.items():
    if freq > 1:
        total_repeated_first_names += freq
        first_name_output += f'First Name: {name}: {freq}\n'
        print(f'First Name: {name}: {freq}')

# Display and add last names occurring more than 1 time to the output string
for name, freq in last_name_freq.items():
    if freq > 1:
        total_repeated_last_names += freq
        last_name_output += f'Last Name: {name}: {freq}\n'
        print(f'Last Name: {name}: {freq}')

# Display and add duplicate lines to the output string
for line, line_numbers in duplicate_line_numbers.items():
    duplicate_line_output += f'Duplicate Line: {line.strip()} | Line Numbers: {", ".join(map(str, line_numbers))}\n'
    print(f'Duplicate Line: {line.strip()} | Line Numbers: {", ".join(map(str, line_numbers))}')

# Calculate the percentages of repeated names
percentage_repeated_first = calculate_percentage(total_repeated_first_names, total_first_names)
percentage_repeated_last = calculate_percentage(total_repeated_last_names, total_last_names)

# Display the name and line totals and percentages
print(f'Total First Names: {total_first_names}')
print(f'Total Repeated First Names: {total_repeated_first_names}')
print(f'Percentage of Repeated First Names: {percentage_repeated_first:.2f}%')
print(f'Total Last Names: {total_last_names}')
print(f'Total Repeated Last Names: {total_repeated_last_names}')
print(f'Percentage of Repeated Last Names: {percentage_repeated_last:.2f}%')

# Prepare the complete statistics output
complete_stats_output = (
    f'Total First Names: {total_first_names}\n'
    f'Total Repeated First Names: {total_repeated_first_names}\n'
    f'Percentage of Repeated First Names: {percentage_repeated_first:.2f}%\n'
    f'Total Last Names: {total_last_names}\n'
    f'Total Repeated Last Names: {total_repeated_last_names}\n'
    f'Percentage of Repeated Last Names: {percentage_repeated_last:.2f}%\n'
    f'\nDuplicate Lines:\n{duplicate_line_output}'
)

# Write the results to stats_complete.txt
write_to_file('stats_complete.txt', complete_stats_output)

# Print a message indicating the completion of writing results
print("Results written to stats_complete.txt")
