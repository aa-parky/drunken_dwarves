import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

# Download the necessary NLTK data (if not already downloaded)
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')


def extract_conjunctions(text):
    words = word_tokenize(text)
    tagged_words = pos_tag(words)

    conjunctions = [word for word, tag in tagged_words if tag == 'CC']
    return conjunctions


def main():
    with open('input.txt', 'r') as input_file:
        text = input_file.read()

    conjunctions = extract_conjunctions(text)

    print("Conjunctions found and their counts:")
    conjunction_count = {}
    for conjunction in conjunctions:
        conjunction_count[conjunction] = conjunction_count.get(conjunction, 0) + 1
        print(conjunction)

    with open('conjunctions_out.txt', 'w') as output_file:
        for conjunction, count in conjunction_count.items():
            output_file.write(f"{conjunction}: {count}\n")


if __name__ == "__main__":
    main()
