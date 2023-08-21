import nltk
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')


def convert_nouns_to_adjectives(text):
    words = word_tokenize(text)
    tagged_words = nltk.pos_tag(words)

    substitution_list = []
    for word, pos in tagged_words:
        if pos.startswith('NN'):  # Checking if the word is a noun
            synonyms = []
            for syn in wordnet.synsets(word, pos=wordnet.NOUN):
                for lemma in syn.lemmas():
                    if lemma.name() != word:
                        synonyms.append(lemma.name())
            if synonyms:
                new_word = synonyms[0]  # You can choose the first synonym here
                substitution_list.append((word, new_word))
        else:
            substitution_list.append((word, None))

    return substitution_list


file_path = 'input.txt'  # Replace with the path to your input file
output_path = 'output.txt'  # Replace with the desired output path

with open(file_path, 'r') as file:
    input_text = file.read()

substitution_list = convert_nouns_to_adjectives(input_text)

with open(output_path, 'w') as file:
    for original_word, substituted_word in substitution_list:
        if substituted_word:
            file.write(f"{original_word} -> {substituted_word}\n")
        else:
            file.write(original_word + "\n")
