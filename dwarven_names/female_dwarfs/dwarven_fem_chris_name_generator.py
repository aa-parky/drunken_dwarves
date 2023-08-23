import random
import datetime

# Read the list of syllables for first name from the syllables.txt file
with open('de_fem_final.txt', 'r') as file:
    syllable_list = [line.strip() for line in file]

# Read the list of syllables for surname from the surname_syllables.txt file
with open('surname_syllables.txt', 'r') as file:
    surname_syllable_list = [line.strip() for line in file]

# Read the list of adjectives from the all_JJ.txt file
with open('all_JJ.txt', 'r') as file:
    adjective_list = [line.strip() for line in file]

# Number of names to generate
num_names = 10

generated_names = []  # To store the generated names

for _ in range(num_names):
    # Generate a random number of syllables between 1 and 3 for first name
    num_syllables_first = random.randint(1, 3)

    # Generate a random number of syllables between 1 and 3 for surname
    num_syllables_surname = random.randint(1, 3)

    # Randomly select syllables for first name
    selected_syllables_first = random.sample(syllable_list, num_syllables_first)
    generated_first_name = ''.join(selected_syllables_first).capitalize()

    # Randomly select syllables for surname
    selected_syllables_surname = random.sample(surname_syllable_list, num_syllables_surname)
    generated_surname = ''.join(selected_syllables_surname).capitalize()

    # Randomly select an adjective and capitalize its first letter
    selected_adjective = random.choice(adjective_list).capitalize()

    # Combine the generated names in the format "FirstName Surname of Adjective"
    final_name = f"{generated_first_name} {generated_surname} the {selected_adjective}"

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
