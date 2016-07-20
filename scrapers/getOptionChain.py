import requests
import pandas as pd

url = 'https://www.nseindia.com/live_market/dynaContent/live_watch/option_chain/optionKeys.jsp?symbol=%s&date=%s'

headers = { 'Accept' : '*/*',
            'User-Agent' : 'Mozilla/5.0',
            'Referer' : 'http://www.nseindia.com',
            'Connection' : 'keep-alive'
            }

fields = ['CE OI', 'CE Chng in OI', 'CE Volume', 'CE IV', 'CE LTP', 'CE Net Chng', 'CE Bid Qty', 'CE Bid Price', 'CE Ask Price', 'CE Ask Qty', 'Strike Price',
          'PE Bid Qty', 'PE Bid Price', 'PE Ask Price', 'PE Ask Qty', 'PE Net Chng', 'PE LTP', 'PE IV', 'PE Volume', 'PE Chng in OI', 'PE OI']

def get_option_chain(symbol, expiry):
    r = requests.get(url % (symbol, expiry), headers=headers).content
    df = pd.read_html(r, attrs= {'id':'octable'})
    df = df[0].dropna(axis=1, how='all')
    df = df[df.columns[1:]]
    df.columns = fields
    return df
    
#get_option_chain('NIFTY', '28JUL2016')
