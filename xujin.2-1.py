import pandas as pd
data = pd.read_csv('nobel.2.1.csv')
print(data.info())
print(data.columns)
nobel_living = data[
    (data['country'].notna ()) & 
    (data['gender'] !=  'org') & 
    (data['died_date'].isna())
]
print(nobel_living.shape)
location_counts = nobel_living['country']. value_counts ()
most_common_location = location_counts.idxmax()
print(f": {most_common_location}")