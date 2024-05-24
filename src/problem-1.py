#
#   Problem 1
#
#   Author: Ernest John Decina
#   Date: 10th May 2024
#
import nltk
from nltk import word_tokenize, sent_tokenize, pos_tag

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

sentence = "Steve Jobs was an American entrepreneur and business magnate. He was the chairman, chief executive officer (CEO), and a co-founder of Apple Inc., chairman and majority shareholder of Pixar, a member of The Walt Disney Company's board of directors following its acquisition of Pixar, and the founder, chairman, and CEO of NeXT. Jobs is widely recognized as a pioneer of the microcomputer revolution of the 1970s and 1980s, along with Apple co-founder Steve Wozniak. "
named_entities = []
pos_tags = {"NNP": []}

# Loop through each word
word_tokens = word_tokenize(sentence)
word_tokens_pos_tag = pos_tag(word_tokens)

for word_token_pos_tag in word_tokens_pos_tag:
    if word_token_pos_tag[1] == "NNP" :
        pos_tags["NNP"].append(word_token_pos_tag[0])
    else:
        if word_token_pos_tag[1] not in pos_tags:
            pos_tags[word_token_pos_tag[1]] = []

        pos_tags[word_token_pos_tag[1]].append(word_token_pos_tag[0]) 
            



print("Parts of Speech Tags")
for key in pos_tags.keys():
    print(key, end="\t")
    print(pos_tags[key], end="\n")



