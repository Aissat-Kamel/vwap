import binance.client
from binance.client import Client
import datetime as dt
import pandas as pd

Pkey = ''
Skey = ''

client = Client(api_key = Pkey, api_secret = Skey)


columns = ['Date','Open','High','Low','Close' ,'Volume','IGNORE','Quote_Volume','Trades_Count','BUY_VOL','BUY_VOL_VAL','x']

def get_klines(ticker, frame, depth):

		klines = client.get_historical_klines(ticker, frame, depth)
		df = pd.DataFrame(klines)
		if not df.empty:
			df.columns = columns
			df['Date'] =  pd.to_datetime(df['Date'],unit='ms')
			df.index = df['Date']
			df["Open"] = pd.to_numeric(df['Open'])
			df["High"] = pd.to_numeric(df['High'])
			df["Low"] = pd.to_numeric(df['Low'])
			df["Close"] = pd.to_numeric(df['Close'])
			df["Volume"] = pd.to_numeric(df['Volume'])
			for i in range(6, len(columns)):
				del df[columns[i]]
			return df
		else:
			return None
