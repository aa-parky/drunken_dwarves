import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

# Download the necessary NLTK data (if not already downloaded)
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')


def extract_determiners(text):
    words = word_tokenize(text)
    tagged_words = pos_tag(words)

    determiners = [word for word, tag in tagged_words if tag == 'DT']
    return determiners


def main():
    with open('input.txt', 'r') as input_file:
        text = input_file.read()

    determiners = extract_determiners(text)

    print("Determiners found and their counts:")
    determiner_count = {}
    for determiner in determiners:
        determiner_count[determiner] = determiner_count.get(determiner, 0) + 1
        print(determiner)

    with open('determiners_out.txt', 'w') as output_file:
        for determiner, count in determiner_count.items():
            output_file.write(f"{determiner}: {count}\n")


if __name__ == "__main__":
    main()
