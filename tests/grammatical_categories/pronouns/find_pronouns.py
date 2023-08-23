import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

# Download the necessary NLTK data (if not already downloaded)
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')


def extract_pronouns(text):
    words = word_tokenize(text)
    tagged_words = pos_tag(words)

    pronouns = [word for word, tag in tagged_words if tag.startswith('PR')]
    return pronouns


def main():
    with open('input.txt', 'r') as input_file:
        text = input_file.read()

    pronouns = extract_pronouns(text)

    print("Pronouns found and their counts:")
    pronoun_count = {}
    for pronoun in pronouns:
        pronoun_count[pronoun] = pronoun_count.get(pronoun, 0) + 1
        print(pronoun)

    with open('pronouns_out.txt', 'w') as output_file:
        for pronoun, count in pronoun_count.items():
            output_file.write(f"{pronoun}: {count}\n")


if __name__ == "__main__":
    main()
