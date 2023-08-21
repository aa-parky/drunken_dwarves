import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')


def get_word_category(word):
    pos_tags = nltk.pos_tag([word])
    return pos_tags[0][1]


def analyze_text(input_text):
    words = word_tokenize(input_text)
    lemmatizer = WordNetLemmatizer()

    analysis_results = []
    for word in words:
        word_category = get_word_category(word)
        lemma = lemmatizer.lemmatize(word)
        analysis_results.append((word, lemma, word_category))

    return analysis_results


input_path = 'input.txt'  # Replace with the path to your input file
output_path = 'output.txt'  # Replace with the desired output path

with open(input_path, 'r') as file:
    input_text = file.read()

analysis_results = analyze_text(input_text)

with open(output_path, 'w') as file:
    for word, lemma, category in analysis_results:
        print(f"Word: {word}, Lemma: {lemma}, Category: {category}")
        file.write(f"Word: {word}, Lemma: {lemma}, Category: {category}\n")
