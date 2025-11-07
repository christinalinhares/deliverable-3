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

#b)
print(data.shape)
#show how many rows and columns

print(data.info())
#gives amount of values for each column, and type of value, object or float

print(data.describe())
#gives count, mean, standard deviation etc for each numerical column


print(data.duplicated().sum())
data = data.drop_duplicates()
#find how many duplicates there are and delete them

#c
data["Genre"] = data["Genre"].fillna("Unknown")
data["Lead Studio"] = data["Lead Studio"].fillna("Unknown")
data["Audience score %"] = data["Audience score %"].fillna(data["Audience score %"].mean())
data["Profitability"] = data["Profitability"].fillna(data["Profitability"].mean())
data["Rotten Tomatoes %"] = data["Rotten Tomatoes %"].fillna(data["Rotten Tomatoes %"].mean())
data["Worldwide Gross"] = data["Worldwide Gross"].fillna(data["Worldwide Gross"].mean())
data["Year"] = data["Year"].fillna(data["Year"].mean())
#since the data set is small rather than removing rows with missing values their values were inputted using the mean for numerical columns to maintain a reasonable size for the data set. If the column did not have numerical values then "Unknown" was inputted into the cell.

#d
#This step is unecessary as no data type needs to be corrected
