import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

# Download the necessary NLTK data (if not already downloaded)
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')


def extract_interjections(text):
    words = word_tokenize(text)
    tagged_words = pos_tag(words)

    interjections = [word for word, tag in tagged_words if tag == 'UH']
    return interjections


def main():
    with open('input.txt', 'r') as input_file:
        text = input_file.read()

    interjections = extract_interjections(text)

    print("Interjections found and their counts:")
    interjection_count = {}
    for interjection in interjections:
        interjection_count[interjection] = interjection_count.get(interjection, 0) + 1
        print(interjection)

    with open('interjections_out.txt', 'w') as output_file:
        for interjection, count in interjection_count.items():
            output_file.write(f"{interjection}: {count}\n")


if __name__ == "__main__":
    main()
