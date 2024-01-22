# Research-Paper
"Can ChatGPT Predicts Indian Stock Market Price Movements". This research paper talks about the potential of ChatGPT in the realm of Indian stock market.

# Gathering Data
I have made GoogleNewsFetch python file for getting the news headlines from google news. It is the optimal method that i have discoverd that was free and would provide the data but it was very hectic task. Here, instead of getting all the news headlines from a single newpaper with all the companies that are listed, i had to get new headlines from a single company and collect it one by one with the filter provided by google news. You can select the date and paste the link from any newpaper (here i have taken The Times of India and The Economic Times) with the company name so that it gives you that exact news from that exasct company at that point of time which is required.  

I then made the list of the companies that are listed in the BSE (Bombay Stiock Exchange) and with the i collected all the newsheadlines accordingly.

# ChatGPT 
For determining the potential of ChatGPT i designed a prompt that we could as the model and with that it would give the result and i stored with the new headlines.
I have used ChatGPT3.0 as it is available free worldwide. The prompt also asks the model the dates of the buying and selling of the stocks in order to get profit. It responds to "YES", "NO" "UNKNOWN", this could also be used for comparing it with other sentiment analysis tools.
As we know ChatGPT3.0 is updated till sept 2019 (it is now updated further but at the time when the process was going on it was not updated), the dataset collected was after sept 2019 so that the model does not have any previous training or knowledge.

# Sentiment Analysis Tool (VARDAR)
It is a famous tool used for sentiment analysis and it is the best as stated in some research papers, so i have compared my results with this tool's results.

# Results
I have plotted the results of one company (Reliance) to showcase how to visualize data. You can do similar results with other companies with the data given.
with the stocks buying and selling we see the profit and loss 
