from nltk.corpus import wordnet


def get_related_adjectives_and_synonyms(word):
    related_words = []

    synsets = wordnet.synsets(word)
    for synset in synsets:
        for lemma in synset.lemmas():
            if lemma.synset().pos() == 'a':
                related_words.append(lemma.name())
            synonyms = [synonym.name() for synonym in lemma.synset().lemmas()]
            related_words.extend(synonyms)

    return related_words


word = "rejoice"
related_words_list = get_related_adjectives_and_synonyms(word)

formatted_output = "\n".join(related_words_list)
print(f"Related Adjectives and Synonyms for '{word}':\n{formatted_output}")
