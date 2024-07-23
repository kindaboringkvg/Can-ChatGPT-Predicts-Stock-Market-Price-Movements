# Research Paper: "Can ChatGPT Predict Indian Stock Market Price Movements?"

This research paper explores the potential of ChatGPT in predicting price movements in the Indian stock market.

## Gathering Data

To gather data, I created a Python script named `GoogleNewsFetch` that retrieves news headlines from Google News. The optimal method I discovered, which is free, required fetching news headlines for each company individually using Google News filters. This allowed me to collect specific news articles from newspapers like The Times of India and The Economic Times for each company listed on the Bombay Stock Exchange (BSE).

## ChatGPT

To determine the potential of ChatGPT, I designed a prompt that queries the model using the news headlines. I used ChatGPT 3.0 for this purpose, as it is freely available worldwide. The prompt asks the model whether to buy or sell stocks on specific dates to achieve a profit, with responses of "YES," "NO," or "UNKNOWN." This can also be compared with other sentiment analysis tools.

Since ChatGPT 3.0 was updated only until September 2019 at the time of my research, I collected data after this date to ensure the model did not have prior knowledge.

## Sentiment Analysis Tool (VADER)

I compared ChatGPT's results with VADER, a well-regarded sentiment analysis tool as mentioned in several research papers.

## Results

I have plotted the results for one company (Reliance) to demonstrate data visualization. You can replicate these results for other companies using the provided data. The plots showcase the profits and losses based on stock buying and selling decisions.

## Repository Contents

This repository holds all the datasets that I collected manually and the scripts used to collect and process the data. To collect the dataset, I used Google News filters set to "All Time" and the `GoogleNewsFetch` Python script. By pasting the news link into the script, it saves the details in a CSV file. Data cleaning may be necessary depending on your specific needs.

The repository also includes result figures and a link to the full research paper. 

You can check my research paper through the link provided [here](add your link here). (If link is not working then it means my paper is still under review sorry!)

This work aims to identify if one can use ChatGPT to predict stock market movements based on news headlines.
