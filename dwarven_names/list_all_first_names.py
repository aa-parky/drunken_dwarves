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

# Display the frequency of each first name
for name, freq in name_freq.items():
    print(f'{name}: {freq}')
