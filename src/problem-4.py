import re
from urllib import request
from bs4 import BeautifulSoup
import nltk
from nltk import word_tokenize, sent_tokenize
from nltk.corpus import stopwords

nltk.download('stopwords')

print("Downloading page")
fp = request.urlopen("https://en.wikipedia.org/wiki/Artificial_intelligence")
mybytes = fp.read()

mystr = mybytes.decode("utf8")
fp.close()

soup = BeautifulSoup(mystr, "html.parser")

output = ''
text_pop = soup.find_all('p')
text = []
for x in text_pop:
    text.append(x.get_text())

# Remove unwanted html elements in string
for t in text:
    # if t.parent.name not in blacklist:
    output += "{} ".format(t)

output.lower()

# Tokenization
print("Creating Tokens")
word_tokens_unclean = word_tokenize(output)
sentence_tokens = sent_tokenize(output)
word_tokens_clean = []
regexp = re.compile('[@_!#$%^&*()<>?/\|}{~:\'.`;,\-[\]]+')

# Clean special chars and stop word
print("Cleaning Data")
stopwords = set(stopwords.words("english"))
for word_token in word_tokens_unclean:
    lower_token = word_token.lower()
    if not regexp.search(lower_token) and lower_token not in stopwords:
        word_tokens_clean.append(lower_token)
        

# Calculate word freuency
print("Calculating word frequency")
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
print("Sorting word frequency")
for indexI in range(len(word_frequency)):
    for indexJ in range(len(word_frequency)):
        if word_frequency[indexI]["frequency"] > word_frequency[indexJ]["frequency"]:
            temp = word_frequency[indexJ]
            word_frequency[indexJ] = word_frequency[indexI]
            word_frequency[indexI] = temp

# Print top 5 most frequent words
print("\nTop 10 most frequent words: ")
for w in word_frequency[:10]:
    print("{}: {}".format(w["value"], w["frequency"]))


# Create Sentence Scores
print("\nCreating scores for scentence")
sentence_scores = {}
for sentence in sentence_tokens:
    word_tokens = word_tokenize(sentence)
    total_word_count = len(word_tokens)
    sentence_scores[sentence] = 0

    for word in word_tokens:
        index = 0
        # Check if word exists
        for word_freq in word_frequency:
            found = False
            if word == word_freq["value"]:
                found = True
                break

            index = index + 1
        
        # Word was not found
        if index > len(word_tokens):
            continue
        
        
        if found:
            
            sentence_scores[sentence] += word_frequency[index]["frequency"]
        else:
            sentence_scores[sentence] = word_frequency[index]["frequency"]
    

    sentence_scores[sentence] /= total_word_count

# Sort sentence scores
print("Sort Sentences")
sorted_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)


print("Creating summary")
summary_length = int(len(sorted_sentences) * 0.3)
summary_sentences = sorted_sentences[:summary_length]
summary = '\n'.join(summary_sentences)

# Print values
print("Summary: \n\n")
print(summary)
            


