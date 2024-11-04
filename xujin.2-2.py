import pandas as pd
from skimpy import skim
df = pd. read_csv("shujuji2.2.csv")
skim (df)
print(df.head())
print(df .describe())
print(df.isnull().sum())
print(df.dtypes)
import matplotlib.pyplot as plt
survival_counts = df[ 'Survived']. value_counts()
survival_counts. plot(kind='bar')
plt. title( 'Survival Counts')
plt. xlabel ('Survived')
plt. ylabel ('Count')
plt.xticks(ticks=[0, 1], labels=['No', 'Yes'], rotation=0)
plt.show
gender_survival = df.groupby(['Sex', 'Survived']). size() .unstack()
gender_survival.plot(kind='bar', stacked=True)
plt. title( 'Survival by Gender')
plt.xlabel ( 'Gender')
plt. ylabel ('Count')
plt.xticks(rotation=0)
plt. show()