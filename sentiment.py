from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer() 

# Try to replace the sentence with the words.text

def print_sentiment_scores(sentence):
    snt = analyzer.polarity_scores(sentence)
    #print(f"{sentence:<40} {str(snt)}")
    compound = snt['compound']
    print(f"the average sentiment score is {compound}")
    #print(snt['compound'])
# Test it with an example
print_sentiment_scores("I dunno it was fine I guess")


