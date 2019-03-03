import pandas as pd
import csv
#df = pd.read_csv("data/output-2015.csv")

#df = df.drop(columns, inplace=True, axis=1)


#df.to_csv("done.csv", encoding='utf-8', index=False)


odata = pd.read_csv('data/output-2015.csv')
odata.drop(['Unnamed: 0','accuracy', 'number_of_results','status','formatted_address','google_place_id','postcode','type' ], axis=1, inplace=True)
odata = odata.dropna()
odata.to_csv('data/output-2015.csv', index=False)

#cleaning more to remove NaN
