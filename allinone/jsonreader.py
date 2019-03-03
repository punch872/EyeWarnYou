import pandas as pd
import json


with open("morning.json") as datafile:
    data = json.load(datafile)
dataframe = pd.DataFrame(data)
