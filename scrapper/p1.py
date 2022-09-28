import nest_asyncio
import twint

nest_asyncio.apply()

def search(search_string:str,query_limit:int):
    config = twint.Config()
    config.Search = search_string
    config.Limit = query_limit
    config.Store_csv = True
    config.Output = search_string + ".csv"
    twint.run.Search(config)


search('bugs bunny',20)
