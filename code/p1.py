import nest_asyncio
import twint
nest_asyncio.apply()

config = twint.Config()
config.Search = "Ukraine"
#config.Location = True
#config.Geo = "48.37,31.16,100"
#config.Lang = "en"
config.Since = '2022-04-01 00:00:00'
config.Until = '2022-05-01 00:00:00'
config.Limit = 1000
config.Store_csv = True
config.Output = "UkraineData.csv"
#running search
twint.run.Search(config)

