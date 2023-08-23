import re
from nltk import FreqDist

# Read the input.txt file
with open('input.txt', 'r') as file:
    text = file.read()

# Extract first names using regular expressions
first_names = re.findall(r'\b\w+\b the', text)

# Remove ' the' from each first name
first_names = [name[:-4] for name in first_names]

# Count the occurrences of each first name
first_name_freq = FreqDist(first_names)

# Initialize variables for first name totals
total_first_names = len(first_names)
total_repeated_first_names = 0

# Prepare a string to hold the first name results
first_name_output = ""

# Display and add first names occurring more than 1 time to the first name output string
for name, freq in first_name_freq.items():
    if freq > 1:
        total_repeated_first_names += freq
        first_name_output += f'{name}: {freq}\n'
        print(f'{name}: {freq}')

# Calculate the percentage of repeated first names
percentage_repeated_first = (total_repeated_first_names / total_first_names) * 100

# Display the first name totals and percentage
print(f'Total First Names: {total_first_names}')
print(f'Total Repeated First Names: {total_repeated_first_names}')
print(f'Percentage of Repeated First Names: {percentage_repeated_first:.2f}%')

# Write the first name results to first_names_output.txt
with open('first_names_output.txt', 'w') as first_names_output_file:
    first_names_output_file.write(first_name_output)
