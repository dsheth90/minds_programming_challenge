# Sentiment Analysis

The objective of this repository is to perform sentiment analysis on Telegram group (Crypto.com) messages between the date of 1st May 2021 to 15th May 2021.
## Installation

To run the project-:
```bash
conda create -n <env_name> python=3.7.0
pip install -r requirements.txt
python3 main.py
```

## Documentation/Explanation
#### Data Gathering-:
1) Collected the data in JSON from the telegram group called Crypto.com between the 1st May to 15th May (Including it).

#### Pre-processing-:
1) Initially load the JSON file and append the text messages and the date into the pandas dataframe after filtering.
2) Some of the texts are stored inside the list and nested dictionary so merged the text into a single string. Though the nested dictionary text only contains "crypto.com" so removed it.
3) Removed the whitespaces and converted all the text into lower case.
4) Checked if the text contains "DOGE" or "SHIB" and only append those texts only.
5) Checked the language of the text and include only English text.
6) Finally, converted the emojis into their equivalent text. We know that emojis are vital for sentiment analysis so used emot library for the same.

#### Compute Sentiment-:
Used TextBlob to compute the sentiment analysis. More details in the Summary portion.

#### Plot-:
1) Used Plotly library to plot the graph.
2) The x-axis represents the days and the y-axis represents the count of that particular day. Also, each bar shows an individual count of positive, negative, and neutral sentiments.
3) This was achieved by grouping the dataframe by day and sentiments and plotting against the total count of each day. 

## Summary/Observations/Results
There are a total of 49436 messages in the JSON file and after filtering, sentiments are computed on 2700 messages. Most of the messages are neutral followed by positive messages. The results were greatly improved by translating emojis into their equivalent texts. The plot clearly summarizes the result. After running main.py, the prediction.csv will be generated which contains filtered text, their respective date, polarize score, and their sentiment. In the browser the plot will be opened once the code will run and on hovering over the bar graph, individual values can be viewed.

Summary of Sentiment analysis library -:
1) Used TextBlob to compute the sentiment analysis. It returns the polarity score which represents positive if greater than zero, neutral is equal to zero, and negative if less than zero. 
2) I have also used Flair, which is a pre-trained embedding-based model but was trained on the movies and products reviews and was giving poor results in our data so dropped it. I have also used Spacy, NLTK, based sentiment analysis but TextBlob is the most accurate and computes results faster.


