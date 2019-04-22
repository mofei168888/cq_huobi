# encoding: UTF-8

try:
    from app.cqhuobi import DataApi
except Exception as e:
    from cqhuobi import DataApi



url = 'wss://api.huobi.pro/ws'
codes = ['btcusdt','ethusdt','xrpusdt','eosusdt','bchusdt','bsvusdt','htusdt','ltcusdt','trxusdt','neousdt','nulseth','dashusdt','zecusdt']

if __name__ == '__main__':

    api = DataApi()
    api.connect(url)
    for i in range(len(codes)):
        api.subscribeMarketDepth(codes[i])
        api.subscribeTradeDetail(codes[i])
        api.subscribeMarketDetail(codes[i])
        api.subscribeKline(codes[i],'1min')
    api.subscribeMarketTickers()
    print('start subscribe')