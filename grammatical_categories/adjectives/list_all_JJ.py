from nltk.corpus import wordnet

adjectives = []

# Loop through each synset in the adjectives section of WordNet
for synset in wordnet.all_synsets(wordnet.ADJ):
    for lemma in synset.lemmas():
        adjectives.append(lemma.name())

# Remove duplicates by converting the list to a set and back to a list
unique_adjectives = list(set(adjectives))

# Write the list of unique adjectives to a file
with open("all_JJ.txt", "w") as file:
    for adj in unique_adjectives:
        file.write(adj + "\n")

print("Adjectives written to all_JJ.txt")
