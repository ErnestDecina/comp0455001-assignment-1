#
#   Problem 1
#
#   Author: Ernest John Decina
#   Date: 10th May 2024
#

from nltk import word_tokenize, sent_tokenize, pos_tag

sentence = "Steve Jobs was an American entrepreneur and business magnate. He was the chairman, chief executive officer (CEO), and a co-founder of Apple Inc., chairman and majority shareholder of Pixar, a member of The Walt Disney Company's board of directors following its acquisition of Pixar, and the founder, chairman, and CEO of NeXT. Jobs is widely recognized as a pioneer of the microcomputer revolution of the 1970s and 1980s, along with Apple co-founder Steve Wozniak. "

# Loop through each word
for sentence_token in sent_tokenize(sentence):
    word_tokens = word_tokenize(sentence_token)
    print(pos_tag(word_tokens), end="\n")
