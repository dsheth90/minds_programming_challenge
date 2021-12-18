import json
import pandas as pd
import langid
from tqdm import tqdm
from emot.emo_unicode import UNICODE_EMOJI
from textblob import TextBlob
import numpy as np
import plotly.express as px


def convert_emojis(text):
    for emot in UNICODE_EMOJI:
        text1 = "_".join(UNICODE_EMOJI[emot].replace(",", "").replace(":", "").split())
        text1 = text1.replace('_', ' ') + ' '
        text = text.replace(emot, text1)
    return text


def pre_process(data):
    df = pd.DataFrame()
    for i in tqdm(range(0, len(data['messages']))):
        tmp_str = ''
        if isinstance(data["messages"][i]["text"], list):
            for txt in data["messages"][i]["text"]:
                if isinstance(txt, dict):
                    pass
                else:
                    tmp_str = tmp_str + txt
        else:
            tmp_str = data["messages"][i]["text"]
        tmp_str = tmp_str.lower().strip()
        if 'doge' in tmp_str or 'shib' in tmp_str:
            language = langid.classify(tmp_str)
            tmp_str = convert_emojis(tmp_str)
            if language[0] == 'en':
                df = df.append({'day': data["messages"][i]["date"][8:10], 'text': tmp_str}, ignore_index=True)
    return df


def compute_sentiment(df):
    df["sentiment_score"] = df["text"].apply(lambda x: TextBlob(str(x)).sentiment.polarity)
    df["sentiment"] = np.select([df["sentiment_score"] < 0, df["sentiment_score"] == 0, df["sentiment_score"] > 0],
                                ['neg', 'neu', 'pos'])
    return df


def plot(df):
    df_grouped = df.groupby(["day", "sentiment"]).count().reset_index()
    fig = px.bar(df_grouped, x=df_grouped['day'], y=df_grouped["text"], color=df_grouped["sentiment"],
                 title="Sentiment analysis per day")
    fig.show()


if __name__ == '__main__':
    f = open('result.json')
    data_json = json.load(f)
    df_preprocessed = pre_process(data_json)
    df_sentiment = compute_sentiment(df_preprocessed)
    plot(df_sentiment)
    df_sentiment.to_csv('prediction.csv', index=False, header=True)
