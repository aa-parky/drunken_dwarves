import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

# Download the necessary NLTK data (if not already downloaded)
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')


def extract_prepositions(text):
    words = word_tokenize(text)
    tagged_words = pos_tag(words)

    prepositions = [word for word, tag in tagged_words if tag == 'IN']
    return prepositions


def main():
    with open('input.txt', 'r') as input_file:
        text = input_file.read()

    prepositions = extract_prepositions(text)

    print("Prepositions found and their counts:")
    preposition_count = {}
    for preposition in prepositions:
        preposition_count[preposition] = preposition_count.get(preposition, 0) + 1
        print(preposition)

    with open('prepositions_out.txt', 'w') as output_file:
        for preposition, count in preposition_count.items():
            output_file.write(f"{preposition}: {count}\n")


if __name__ == "__main__":
    main()
