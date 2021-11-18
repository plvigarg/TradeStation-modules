stocks = ["CIPLA", "ASIANPAINT", "HDFCBANK", "HCLTECH", "BRITANNIA",
          "HEROMOTOCO", "AXISBANK", "BHARTIARTL", "GAIL", "BAJFINANCE", "ICICIBANK",
          "INDUSINDBK", "INFY", "MARUTI", "SBIN", "RELIANCE", "TCS", "TATASTEEL",
          "TITAN", "TATAMOTORS"]

from senti_helper import predict_sentiment
from collections import Counter
import pickle

parameters = [
    {
        'query': '(CIPLA) (lang:en)',
        'max_results': '100',
        'tweet.fields': 'created_at,lang'
    },
    {
        'query': '(ASIANPAINT) (lang:en)',
        'max_results': '100',
        'tweet.fields': 'created_at,lang'
    },
    {
        'query': '(HDFCBANK) (lang:en)',
        'max_results': '100',
        'tweet.fields': 'created_at,lang'
    },
    {
        'query': '(HCLTECH) (lang:en)',
        'max_results': '100',
        'tweet.fields': 'created_at,lang'
    },
    {
        'query': '(BRITANNIA) (lang:en)',
        'max_results': '100',
        'tweet.fields': 'created_at,lang'
    },
    {
        'query': '(HEROMOTOCO or HEROMOTO) (lang:en)',
        'max_results': '100',
        'tweet.fields': 'created_at,lang'
    },
    {
        'query': '(AXISBANK) (lang:en)',
        'max_results': '100',
        'tweet.fields': 'created_at,lang'
    },
    {
        'query': '(BHARTIARTL) (lang:en)',
        'max_results': '100',
        'tweet.fields': 'created_at,lang'
    },
    {
        'query': '(GAIL) (lang:en)',
        'max_results': '100',
        'tweet.fields': 'created_at,lang'
    },
    {
        'query': '(BAJFINANCE OR BAJAJ FINANCE) (lang:en)',
        'max_results': '100',
        'tweet.fields': 'created_at,lang'
    },
    {
        'query': '(ICICIBANK) (lang:en)',
        'max_results': '100',
        'tweet.fields': 'created_at,lang'
    },
    {
        'query': '(INDUSINDBK OR INDUS INDIA BANK) (lang:en)',
        'max_results': '100',
        'tweet.fields': 'created_at,lang'
    },
    {
        'query': '(INFY OR INFOSYS) (lang:en)',
        'max_results': '100',
        'tweet.fields': 'created_at,lang'
    },
    {
        'query': '(MARUTI) (lang:en)',
        'max_results': '100',
        'tweet.fields': 'created_at,lang'
    },
    {
        'query': '(SBIN OR STATE BANK OF INDIA) (lang:en)',
        'max_results': '100',
        'tweet.fields': 'created_at,lang'
    },
    {
        'query': '(RELIANCE) (lang:en)',
        'max_results': '100',
        'tweet.fields': 'created_at,lang'
    },
    {
        'query': '(TCS) (lang:en)',
        'max_results': '100',
        'tweet.fields': 'created_at,lang'
    },
    {
        'query': '(TATASTEEL) (lang:en)',
        'max_results': '100',
        'tweet.fields': 'created_at,lang'
    },
    {
        'query': '(TITAN) (lang:en)',
        'max_results': '100',
        'tweet.fields': 'created_at,lang'
    },
    {
        'query': '(TATAMOTORS) (lang:en)',
        'max_results': '100',
        'tweet.fields': 'created_at,lang'
    }]


def get_predictions():
    predictions = {}

    for i, stk in enumerate(stocks):
        # print(parameters[i])
        idx, le = predict_sentiment(parameters[i], stk)
        pos = Counter(idx)['POSITIVE']
        neg = Counter(idx)['NEGATIVE']

        negper = (neg/le)*100
        posper = (pos/le)*100
        change = posper-negper
        predictions[stk] = change

        print(stk, predictions[stk])

    open_file = open("dictionary.pkl", "wb")
    pickle.dump(predictions, open_file)
    open_file.close()


# get_predictions()
