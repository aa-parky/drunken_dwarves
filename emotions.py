from nltk.corpus import wordnet


def get_emotion_related_words(emotion):
    emotion_related_words = []

    for pos in ['n', 'v', 'a', 'r']:  # 'n' for noun, 'v' for verb, 'a' for adjective, 'r' for adverb
        wordnet_pos = None
        if pos == 'n':
            wordnet_pos = wordnet.NOUN
        elif pos == 'v':
            wordnet_pos = wordnet.VERB
        elif pos == 'a':
            wordnet_pos = wordnet.ADJ
        elif pos == 'r':
            wordnet_pos = wordnet.ADV

        if wordnet_pos:
            synsets = wordnet.synsets(emotion, pos=wordnet_pos)

            for synset in synsets:
                for lemma in synset.lemmas():
                    word = lemma.name()
                    lemma_word = lemma.synset().lemmas()[0].name()
                    category = pos
                    emotion_related_words.append((word, lemma_word, category))

    return emotion_related_words


emotion = "rejoice"
emotion_words = get_emotion_related_words(emotion)

for word, lemma, category in emotion_words:
    print(f"Word: {word}, Lemma: {lemma}, Category: {category}")
