import re
from nltk import FreqDist
from nltk.tokenize import word_tokenize

# Read the input.txt file
with open('input.txt', 'r') as file:
    text = file.read()

# Extract first names using regular expressions
first_names = re.findall(r'\b\w+\b the', text)

# Remove ' the' from each first name
first_names = [name[:-4] for name in first_names]

# Count the occurrences of each first name
name_freq = FreqDist(first_names)

# Sort the frequency distribution by count in descending order
sorted_name_freq = sorted(name_freq.items(), key=lambda x: x[1], reverse=True)

# Calculate the total number of first names
total_first_names = len(first_names)

# Open the output file for writing
with open('list_all_first_names.txt', 'w') as output_file:
    # Display the header in console
    print(f"{'Name':<20}{'Count':<10}{'Percentage':<15}")
    print("=" * 45)

    # Write the header to the file
    output_file.write(f"{'Name':<20}{'Count':<10}{'Percentage':<15}\n")
    output_file.write("=" * 45 + "\n")

    # Display and write each first name, count, and percentage
    for name, freq in sorted_name_freq:
        percentage = (freq / total_first_names) * 100
        print(f"{name:<20}{freq:<10}{percentage:.2f}%")
        output_file.write(f"{name:<20}{freq:<10}{percentage:.2f}%\n")
