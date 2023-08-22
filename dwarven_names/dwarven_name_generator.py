import random
import datetime

# Read the list of syllables from the syllables.txt file
with open('syllables.txt', 'r') as file:
    syllable_list = [line.strip() for line in file]

# Read the list of adjectives from the all_JJ.txt file
with open('all_JJ.txt', 'r') as file:
    adjective_list = [line.strip() for line in file]

# Number of names to generate
num_names = 1000

generated_names = []  # To store the generated names

for _ in range(num_names):
    # Generate a random number of syllables between 1 and 3
    num_syllables = random.randint(1, 3)

    # Randomly select syllables from the list
    selected_syllables = random.sample(syllable_list, num_syllables)

    # Combine the syllables to form a name
    generated_name = ''.join(selected_syllables)

    # Capitalize only the first letter of the generated name
    capitalized_name = generated_name.capitalize()

    # Randomly select an adjective from the list and capitalize its first letter
    selected_adjective = random.choice(adjective_list)
    capitalized_adjective = selected_adjective.capitalize()

    # Combine the adjective and name in the format "Name the Adjective"
    final_name = f"{capitalized_name} the {capitalized_adjective}"

    generated_names.append(final_name)  # Store the generated name

    print("Generated Name:", final_name)

# Create a filename based on date and time
current_datetime = datetime.datetime.now()
filename = current_datetime.strftime("%Y-%m-%d_%H-%M-%S") + "_generated_names.txt"

# Write the generated names to the file
with open(filename, 'w') as output_file:
    for name in generated_names:
        output_file.write(name + '\n')

print("Generated names have been saved to:", filename)
