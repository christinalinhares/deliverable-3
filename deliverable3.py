print("deliverable 3")
import pandas as pd
import seaborn as sns

data = pd.read_csv("movies.csv")

#2 Preliminary steps
#a)
top_5_worldwide_gross = data["Worldwide Gross"].value_counts().head(5)
print(top_5_worldwide_gross)

top_5_audience_score = data["Audience score %"].value_counts().head(5)
print(top_5_audience_score)
#showing top 5 values of worldwide gross and audience score within dataset

print(data.shape)
#show how many rows and columns

print(data.info())
#gives amount of values for each column, and type of value, object or float

print(data.describe())
# gives count, mean, standard deviation etc for each numerical column

