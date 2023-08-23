import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

# Download the necessary NLTK data (if not already downloaded)
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')


def extract_nouns(text):
    words = word_tokenize(text)
    tagged_words = pos_tag(words)

    nouns = [word for word, tag in tagged_words if tag.startswith('N')]
    return nouns


def main():
    with open('input.txt', 'r') as input_file:
        text = input_file.read()

    nouns = extract_nouns(text)

    print("Nouns found and their counts:")
    noun_count = {}
    for noun in nouns:
        noun_count[noun] = noun_count.get(noun, 0) + 1
        print(noun)

    with open('nouns_out.txt', 'w') as output_file:
        for noun, count in noun_count.items():
            output_file.write(f"{noun}: {count}\n")


if __name__ == "__main__":
    main()
