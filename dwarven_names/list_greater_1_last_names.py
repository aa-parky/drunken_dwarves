import re
from nltk import FreqDist

# Read the input.txt file
with open('input.txt', 'r') as file:
    text = file.read()

# Extract last names using regular expressions
last_names = re.findall(r'the (\w+)', text)

# Count the occurrences of each last name
last_name_freq = FreqDist(last_names)

# Initialize variables for last name totals
total_last_names = len(last_names)
total_repeated_last_names = 0

# Prepare a string to hold the last name results
last_name_output = ""

# Display and add last names occurring more than 1 time to the last name output string
for name, freq in last_name_freq.items():
    if freq > 1:
        total_repeated_last_names += freq
        last_name_output += f'{name}: {freq}\n'
        print(f'{name}: {freq}')

# Calculate the percentage of repeated last names
percentage_repeated_last = (total_repeated_last_names / total_last_names) * 100

# Display the last name totals and percentage
print(f'Total Last Names: {total_last_names}')
print(f'Total Repeated Last Names: {total_repeated_last_names}')
print(f'Percentage of Repeated Last Names: {percentage_repeated_last:.2f}%')

# Write the last name results to last_names_output.txt
with open('last_names_output.txt', 'w') as last_names_output_file:
    last_names_output_file.write(last_name_output)
