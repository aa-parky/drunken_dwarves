import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

# Download the necessary NLTK data (if not already downloaded)
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')


def extract_adjectives(text):
    words = word_tokenize(text)
    tagged_words = pos_tag(words)

    adjectives = [word for word, tag in tagged_words if tag.startswith('JJ')]
    return adjectives


def main():
    with open('input.txt', 'r') as input_file:
        text = input_file.read()

    adjectives = extract_adjectives(text)

    print("Adjectives found and their counts:")
    adjective_count = {}
    for adjective in adjectives:
        adjective_count[adjective] = adjective_count.get(adjective, 0) + 1
        print(adjective)

    with open('adjectives_out.txt', 'w') as output_file:
        for adjective, count in adjective_count.items():
            output_file.write(f"{adjective}: {count}\n")


if __name__ == "__main__":
    main()
