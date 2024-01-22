import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

input_file = 'INSERT PATH OF CSV FILE'  

df = pd.read_csv(input_file)

def analyze_sentiment(text):
    sentiment = analyzer.polarity_scores(text)
    compound_score = sentiment['compound']
    
    if compound_score >= 0.05:
        return "Positive"
    elif compound_score <= -0.05:
        return "Negative"
    else:
        return "Neutral"

# Apply sentiment analysis to the "headline" column and store results in a new column
df['vaderSentiment'] = df['headline'].apply(analyze_sentiment)

# Save the DataFrame with sentiment analysis results to the same input CSV file
df.to_csv(input_file, index=False)

print(f'Sentiment analysis results saved to {input_file}')
