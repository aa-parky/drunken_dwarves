import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

# Download the necessary NLTK data (if not already downloaded)
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')


def extract_adverbs(text):
    words = word_tokenize(text)
    tagged_words = pos_tag(words)

    adverbs = [word for word, tag in tagged_words if tag.startswith('RB')]
    return adverbs


def main():
    with open('input.txt', 'r') as input_file:
        text = input_file.read()

    adverbs = extract_adverbs(text)

    print("Adverbs found and their counts:")
    adverb_count = {}
    for adverb in adverbs:
        adverb_count[adverb] = adverb_count.get(adverb, 0) + 1
        print(adverb)

    with open('adverbs_out.txt', 'w') as output_file:
        for adverb, count in adverb_count.items():
            output_file.write(f"{adverb}: {count}\n")


if __name__ == "__main__":
    main()
