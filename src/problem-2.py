#
#   Problem 2
#
#   Author: Ernest John Decina
#   Date: 13th May 2024
#

from nltk import bigrams, trigrams, word_tokenize


# Tokenize text
text = "Machine learning is a necessary field in today's world. Data science can do wonders. Natural Language Processing is how machines understand text"
tokens = word_tokenize(text)

bigram_result = bigrams(tokens)
trigram_result = trigrams(tokens)


print("Bigram result: ")
for bigram in bigram_result:
    print(bigram)

print()

print("Trigram result: ")
for trigram in trigram_result:
    print(trigram)
