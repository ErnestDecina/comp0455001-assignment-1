import re
from urllib import request
from bs4 import BeautifulSoup
from nltk import word_tokenize, sent_tokenize


fp = request.urlopen("https://en.wikipedia.org/wiki/Artificial_intelligence")
mybytes = fp.read()

mystr = mybytes.decode("utf8")
fp.close()

soup = BeautifulSoup(mystr)

output = ''
blacklist = [
    '[document]',
   'noscript',
    'header',
    'html',
    'meta',
    'head', 
    'input',
    'script',
    "style"
    # there may be more elements you don't want, such as "style", etc.
]

text = soup.find_all(text=True)

# Remove unwanted html elements in string
for t in text:
    if t.parent.name not in blacklist:
        output += "{} ".format(t)

output.lower()

# Tokenization
word_tokens_unclean = word_tokenize(output)
sentence_tokens = sent_tokenize(output)
word_tokens_clean = []
regexp = re.compile('[@_!#$%^&*()<>?/\|}{~:\'.`;,\-[\]]+')

# Clean special chars and stop word
stopwords = ["the", "a", "about", "above", "after", "again", "against", "all", "am", "an", "and", "any", "are", "aren't", "as", "at", "be", "because", "been", "before", "being", "below", "between", "both", "but", "by", "can't", "cannot", "could", "couldn't", "did", "didn't", "do", "does", "doesn't", "doing", "don't", "down", "during", "each", "few", "for", "from", "further", "had", "hadn't", "has", "hasn't", "have", "haven't", "having", "he", "he'd", "he'll", "he's", "her", "here", "here's", "hers", "herself", "him", "himself", "his", "how", "how's", "i", "i'd", "i'll", "i'm", "i've", "if", "in", "into", "is", "isn't", "it", "it's", "its", "itself", "let's", "me", "more", "most", "mustn't", "my", "myself", "no", "nor", "not", "of", "off", "on", "once", "only", "or", "other", "ought", "our", "ours    ourselves", "out", "over", "own", "same", "shan't", "she", "she'd", "she'll", "she's", "should", "shouldn't", "so", "some", "such", "than", "that", "that's", "the", "their", "theirs", "them", "themselves", "then", "there", "there's", "these", "they", "they'd", "they'll", "they're", "they've", "this", "those", "through", "to", "too", "under", "until", "up", "very", "was", "wasn't", "we", "we'd", "we'll", "we're", "we've", "were", "weren't", "what", "what's", "when", "when's", "where", "where's", "which", "while", "who", "who's", "whom", "why", "why's", "with", "won't", "would", "wouldn't", "you", "you'd", "you'll", "you're", "you've", "your", "yours", "yourself", "yourselves"]
for word_token in word_tokens_unclean:
    if not regexp.search(word_token) and word_token not in stopwords:
        word_tokens_clean.append(word_token.lower())
        

# Calculate word freuency
word_frequency = []
for word_token in word_tokens_clean:
    found = False
    index = 0

    # Check if word already exists in the word_frequency
    for word in word_frequency:
        if word_token == word["value"]:
            found = True
            break

        index = index + 1
    
    if found:
        word_frequency[index]["frequency"] = word_frequency[index]["frequency"] + 1
    else:
        new_word = {"value" : word_token, "frequency": 1}
        word_frequency.append(new_word)

# Sort values in descending order
for indexI in range(len(word_frequency)):
    for indexJ in range(len(word_frequency)):
        if word_frequency[indexI]["frequency"] < word_frequency[indexJ]["frequency"]:
            temp = word_frequency[indexJ]
            word_frequency[indexJ] = word_frequency[indexI]
            word_frequency[indexI] = temp


# Print values
for word in word_frequency:
    print("{} : {}".format(word["value"], word["frequency"]))
            


