from nltk.corpus import wordnet


def get_related_adjectives_and_synonyms(word):
    related_words = set()  # Use a set to automatically remove duplicates

    synsets = wordnet.synsets(word)
    for synset in synsets:
        for lemma in synset.lemmas():
            if lemma.synset().pos() == 'a':
                related_words.add((lemma.name(), 'adjective'))
            synonyms = [(synonym.name(), synonym.synset().pos()) for synonym in lemma.synset().lemmas()]
            related_words.update(synonyms)  # Use update() to add multiple elements to the set

    return related_words


word = "triumph"
related_words_set = get_related_adjectives_and_synonyms(word)

formatted_output = "\n".join([f"{word} ({category})" for word, category in related_words_set])
print(f"Related Adjectives and Synonyms for '{word}':\n{formatted_output}")
