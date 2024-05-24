from nltk import *
from nltk.corpus import *

sentences = [
    "Solen skinner i dag, fuglene synger, og det er sommer.",
    "Ní dhéanfaidh ach Dia breithiúnas orm.",
    "I domum et cuna matrem tuam in cochleare.",
    "Huffa, huffa meg, det finns poteter på badet. Stakkars, stakkars meg, det finns poteter på badet."
]
languages = stopwords.fileids()

def language_stopword_tally(input):
    stopword_tally={}
    tokens = word_tokenize(input)
    sentence_words = []

    # Make all words lower case
    for word in tokens:
        sentence_words.append(word.lower())
    
    # Loop for all languages supported by nltk
    for language in languages:
        # Get stop words for current langugae
        language_stopwords = set(stopwords.words(language))

        # Convert list to a set
        sentence_words = set(sentence_words)

        # Find the intersection of the stopwords and words
        same_words = sentence_words.intersection(language_stopwords)

        # Add to dictionary of tallys
        stopword_tally[language] = len(same_words)

    return stopword_tally 

def language_detect(input):
    # Get tally for sentence
    tally = language_stopword_tally(input)

    # Get highest value
    lang = max(tally, key=tally.get)
    return {"lang": lang, "probabilty" : tally}

# Loop for all sentences
for sentence in sentences:
    probable_language = language_detect(sentence)
    print("\n\nSentence: {}".format(sentence))
    print("Language: {}".format(probable_language["lang"]))

    print("Probabilty: {}".format(probable_language["probabilty"]))

