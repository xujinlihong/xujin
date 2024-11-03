import pandas as pd
data = pd.read_csv('seattle_pet.1.csv')
num_pets = data. shape [0]
print(f" {num_pets}")
num_variables = data.shape [1]
print(f" {num_variables}")
name_counts = data['animal_s_name']. value_counts()
top_three_names = name_counts. head (3)
print (top_three_names)