import nest_asyncio
import twint
nest_asyncio.apply()

config = twint.Config()
config.Search = "btc"
config.Lang = "en"
config.Since = '2016-01-01 00:00:00'
config.Until = '2016-01-26 00:00:00'
config.Store_csv = True
config.Output = "BTCtweet.csv"
#running search
twint.run.Search(config)

