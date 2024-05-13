#
#   Problem 3
#
#   Author: Ernest John Decina
#   Date: 13th May 2024
#


from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


sentences = [
    "We are happy!",
    "Today I am Happy",
    "The best life ever",
    "I am sad",
    "We are sad",
    "We are super sad",
    "We are all so sad today"
]



def getSentiment(sentence: str) -> str:
    sentiment_intensity_analyzer = SentimentIntensityAnalyzer()

    sentence_sentiment_result_dict = sentiment_intensity_analyzer.polarity_scores(sentence)
    
    if sentence_sentiment_result_dict["compound"] >= 0.05:
        return "Positive"
    
    elif sentence_sentiment_result_dict["compound"] <= -0.05:
        return "Negative"
    
    else:
        return "Neutral"

    pass

for sentence in sentences:
    print(sentence)
    print("Sentiment: ", getSentiment(sentence))
    print()
