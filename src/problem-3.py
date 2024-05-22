#
#   Problem 3
#
#   Author: Ernest John Decina
#   Date: 13th May 2024
#


from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from nltk import word_tokenize


sentences = [
    "We are happy!",
    "Today I am Happy",
    "The best life ever",
    "I am sad",
    "We are sad",
    "We are super sad",
    "We are all so sad today"
]

def getSentimentToken(sentence: str) -> list:
    results = []
    sentiment_intensity_analyzer = SentimentIntensityAnalyzer()
    word_tokens = word_tokenize(sentence)

    for word_token in word_tokens:
        tempDict = {word_token: sentiment_intensity_analyzer.polarity_scores(word_token)}
        results.append(tempDict)

    return results


def getSentimentSentence(sentence: str) -> str:
    sentiment_intensity_analyzer = SentimentIntensityAnalyzer()

    sentence_sentiment_result_dict = sentiment_intensity_analyzer.polarity_scores(sentence)
    
    if sentence_sentiment_result_dict["compound"] >= 0.05:
        return "Positive {}".format(sentence_sentiment_result_dict["compound"])
    
    elif sentence_sentiment_result_dict["compound"] <= -0.05:
        return "Negative {}".format(sentence_sentiment_result_dict["compound"])
    
    else:
        return "Neutral {}".format(sentence_sentiment_result_dict["compound"])

    pass

for sentence in sentences:
    print(sentence)
    print("Sentiment: ", getSentimentSentence(sentence))
    print("Token Polarity: ")
    sentimentTokenResults = getSentimentToken(sentence)
    for token in sentimentTokenResults:
        print(token)

    print()
