from nltk.corpus import wordnet


# Function to get related adjectives and synonyms for a given word
def get_related_adjectives_and_synonyms(word):
    related_words = set()  # Use a set to automatically remove duplicates

    synsets = wordnet.synsets(word)
    for synset in synsets:
        for lemma in synset.lemmas():
            # Check if the lemma is an adjective
            if lemma.synset().pos() == 'a':
                related_words.add((lemma.name(), 'adjective'))

            # Get synonyms for the lemma and their parts of speech
            synonyms = [(synonym.name(), synonym.synset().pos()) for synonym in lemma.synset().lemmas()]
            related_words.update(synonyms)  # Use update() to add multiple elements to the set

    return related_words


def main():
    word = "triumph"
    related_words_set = get_related_adjectives_and_synonyms(word)

    # Format the output
    formatted_output = "\n".join([f"{word} ({category})" for word, category in related_words_set])
    print(f"Related Adjectives and Synonyms for '{word}':\n{formatted_output}")


if __name__ == "__main__":
    main()
