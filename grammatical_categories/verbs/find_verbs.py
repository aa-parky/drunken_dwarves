import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

# Download the necessary NLTK data (if not already downloaded)
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')


def extract_verbs(text):
    words = word_tokenize(text)
    tagged_words = pos_tag(words)

    verbs = [word for word, tag in tagged_words if tag.startswith('VB')]
    return verbs


def main():
    with open('input.txt', 'r') as input_file:
        text = input_file.read()

    verbs = extract_verbs(text)

    print("Verbs found and their counts:")
    verb_count = {}
    for verb in verbs:
        verb_count[verb] = verb_count.get(verb, 0) + 1
        print(verb)

    with open('verbs_out.txt', 'w') as output_file:
        for verb, count in verb_count.items():
            output_file.write(f"{verb}: {count}\n")


if __name__ == "__main__":
    main()
