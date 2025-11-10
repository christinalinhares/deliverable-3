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


print("Duplicates:", data.duplicated().sum())
data = data.drop_duplicates()
#find how many duplicates there are and delete them

#c
#data["Genre"] = data["Genre"].fillna("Unknown")
#data["Lead Studio"] = data["Lead Studio"].fillna("Unknown")
#data["Audience score %"] = data["Audience score %"].fillna(data["Audience score %"].mean())
#data["Profitability"] = data["Profitability"].fillna(data["Profitability"].mean())
#data["Rotten Tomatoes %"] = data["Rotten Tomatoes %"].fillna(data["Rotten Tomatoes %"].mean())
#data["Worldwide Gross"] = data["Worldwide Gross"].fillna(data["Worldwide Gross"].mean())
#data["Year"] = data["Year"].fillna(data["Year"].mean())
#since the data set is small rather than removing rows with missing values their values were inputted using the mean for numerical columns to maintain a reasonable size for the data set. If the column did not have numerical values then "Unknown" was inputted into the cell.

#d
#This step is unecessary as no data type needs to be corrected

#3 Univariate non-graphical EDA
#numerical columns
#Audience score %
print("Audience score EDA")
print("Mean:", data["Audience score %"].mean())
print("Median:", data["Audience score %"].median())
print("Mode:", data["Audience score %"].mode().values)
print("Standard deviation", data["Audience score %"].std())
print("Variance:", data["Audience score %"].var())
print("Skewness:", data["Audience score %"].skew())
print("Kurtosis:", data["Audience score %"].kurt())
print("Quartiles:\n", data["Audience score %"].quantile([0.25, 0.5, 0.75]))

#Profitability
print("Profitability EDA")
print("Mean:", data["Profitability"].mean())
print("Median:", data["Profitability"].median())
print("Mode:", data["Profitability"].mode().values)
print("Standard deviation", data["Profitability"].std())
print("Variance:", data["Profitability"].var())
print("Skewness:", data["Profitability"].skew())
print("Kurtosis:", data["Profitability"].kurt())
print("Quartiles:\n", data["Profitability"].quantile([0.25, 0.5, 0.75]))

#Rotten Tomatoes %
print("Rotten Tomatoes % EDA")
print("Mean:", data["Rotten Tomatoes %"].mean())
print("Median:", data["Rotten Tomatoes %"].median())
print("Mode:", data["Rotten Tomatoes %"].mode().values)
print("Standard deviation", data["Rotten Tomatoes %"].std())
print("Variance:", data["Rotten Tomatoes %"].var())
print("Skewness:", data["Rotten Tomatoes %"].skew())
print("Kurtosis:", data["Rotten Tomatoes %"].kurt())
print("Quartiles:\n", data["Rotten Tomatoes %"].quantile([0.25, 0.5, 0.75]))

#Worldwide Gross
#print("Worldwide Gross EDA")
#print("Mean:", data["Worldwide Gross"].mean())
#print("Median:", data["Worldwide Gross"].median())
#print("Mode:", data["Worldwide Gross"].mode().values)
#print("Standard deviation", data["Worldwide Gross"].std())
#print("Variance:", data["Worldwide Gross"].var())
#print("Skewness:", data["Worldwide Gross"].skew())
#print("Kurtosis:", data["Worldwide Gross"].kurt())
#print("Quartiles:\n", data["Worldwide Gross"].quantile([0.25, 0.5, 0.75]))

#Year
print("Year EDA")
print("Mean:", data["Year"].mean())
print("Median:", data["Year"].median())
print("Mode:", data["Year"].mode().values)
print("Standard deviation", data["Year"].std())
print("Variance:", data["Year"].var())
print("Skewness:", data["Year"].skew())
print("Kurtosis:", data["Year"].kurt())
print("Quartiles:\n", data["Year"].quantile([0.25, 0.5, 0.75]))

#non numerical columns
#Film
print("Film EDA")
print("Frequency counts:", data["Film"].value_counts())
#print("Proportion:", data["Film"])
print("Mode:", data["Film"].mode().values)
print("Unique values:", data["Film"].nunique())

#Genre
print("Genre EDA")
print("Frequency counts:", data["Genre"].value_counts())
#print("Proportion:", data["Genre"])
print("Mode:", data["Genre"].mode().values)
print("Unique values:", data["Genre"].nunique())

#Lead Studio
print("Lead Studio EDA")
print("Frequency counts:", data["Lead Studio"].value_counts())
#print("Proportion:", data["Lead Studio"])
print("Mode:", data["Lead Studio"].mode().values)
print("Unique values:", data["Lead Studio"].nunique())


#4:Univariate graphical EDA

#Audience score %

#a) Custom and appropriate number of bins

sns.displot(data, x="Audience score %", bins=20)

#b) Conditioning on other variables

sns.displot(data, x="Audience score %", hue="Genre", element="step")

#c) Stacked histogram

sns.displot(data, x="Audience score %", hue="Genre", multiple="stack")

# (d) Dodge bars

sns.displot(data, x="Audience score %", hue="Genre", multiple="dodge")

# (e) Normalized histogram statistics

sns.displot(data, x="Audience score %", hue="Genre", stat="density", common_norm=False)

# (f) Kernel density estimation

sns.displot(data, x="Audience score %", kind="kde")

# (g) Empirical cumulative distribution

sns.displot(data, x="Audience score %", hue="Genre", kind="ecdf")


#Profitability

#a) Custom and appropriate number of bins

sns.displot(data, x="Profitability", bins=15)

#b) Conditioning on other variables

sns.displot(data, x="Profitability", hue="Lead Studio", element="step")

#c) Stacked histogram

sns.displot(data, x="Profitability", hue="Lead Studio", multiple="stack")

# (d) Dodge bars

sns.displot(data, x="Profitability", hue="Lead Studio", multiple="dodge")

# (e) Normalized histogram statistics

sns.displot(data, x="Profitability", hue="Lead Studio", stat="density", common_norm=False)

# (f) Kernel density estimation

sns.displot(data, x="Profitability", kind="kde")

# (g) Empirical cumulative distribution

sns.displot(data, x="Profitability", hue="Lead Studio", kind="ecdf")


#Rotten Tomatoes %

#a) Custom and appropriate number of bins

sns.displot(data, x="Rotten Tomatoes %", bins=20)

#b) Conditioning on other variables

sns.displot(data, x="Rotten Tomatoes %", hue="Genre", element="step")

#c) Stacked histogram

sns.displot(data, x="Rotten Tomatoes %", hue="Genre", multiple="stack")

# (d) Dodge bars

sns.displot(data, x="Rotten Tomatoes %", hue="Genre", multiple="dodge")

# (e) Normalized histogram statistics

sns.displot(data, x="Rotten Tomatoes %", hue="Genre", stat="density", common_norm=False)

# (f) Kernel density estimation

sns.displot(data, x="Rotten Tomatoes %", kind="kde")

# (g) Empirical cumulative distribution

sns.displot(data, x="Rotten Tomatoes %", hue="Genre", kind="ecdf")



#Worldwide Gross

data["Worldwide Gross"] = data["Worldwide Gross"].replace('\$', '', regex=True).astype(float)
#a) Custom and appropriate number of bins

sns.displot(data, x="Worldwide Gross", bins=15)

#b) Conditioning on other variables

sns.displot(data, x="Worldwide Gross", hue="Lead Studio", element="step")

#c) Stacked histogram

sns.displot(data, x="Worldwide Gross", hue="Lead Studio", multiple="stack")

# (d) Dodge bars

sns.displot(data, x="Worldwide Gross", hue="Lead Studio", multiple="dodge")

# (e) Normalized histogram statistics

sns.displot(data, x="Worldwide Gross", hue="Lead Studio", stat="density", common_norm=False)

# (f) Kernel density estimation

sns.displot(data, x="Worldwide Gross", kind="kde")

# (g) Empirical cumulative distribution

sns.displot(data, x="Worldwide Gross", hue="Lead Studio", kind="ecdf")


#Year

#a) Custom and appropriate number of bins

sns.displot(data, x="Year", discrete=True)

#b) Conditioning on other variables

sns.displot(data, x="Year", hue="Genre", element="step", discrete=True)

#c) Stacked histogram

sns.displot(data, x="Year", hue="Genre", multiple="stack", discrete=True)

# (d) Dodge bars

sns.displot(data, x="Year", hue="Genre", multiple="dodge", discrete=True)

# (e) Normalized histogram statistics

sns.displot(data, x="Year", hue="Genre", stat="density", common_norm=False, discrete=True)

# (f) Kernel density estimation

#not apllicable, KDE is only for continuous numeric data

# (g) Empirical cumulative distribution

sns.displot(data, x="Year", hue="Genre", kind="ecdf")


# post plotting questions for #4

#Rotten tomatoes %









#5. Multivariate non-graphical EDA 
#a) 3 different ways crosstab
#a. 1 
crosstab_1=pd.crosstab(data["Genre"],data["Rotten Tomatoes %"])
print(crosstab_1)
#This table shows the distribution of rotten tomatoes scores across different genres. From the table, we can see that certain genres like animation have higher reviews and are more consistently well reviewed, while genres like comedy or romance have more variability in ratings(mix of low and high scores) indicating more mixed critical reviews.   

#a. 2
crosstab_2=pd.crosstab(data["Audience score %"],data["Profitability"])
print(crosstab_2)
#This shows the relationship between the audience score and the movie profitability. Each number shows how many movies had a certain audience rating and a certain level of profit. It tells us that movies with higher audience scores often have more profitability.

#a. 3
crosstab_3=pd.crosstab(data["Lead Studio"],data["Year"])
print(crosstab_3)
#This crosstab shows how many movies each lead studio released per year. As we can see, large studios like Disney, Warner Bros., and Universal released movies every year which shows how consistent they are. Smaller studios like Lionsgate, Weinstein Company and 20th Century Fox had fewer released per year which shows the low consistence.


#b)

#b. 1 
crosstab_1_percent=pd.crosstab(data["Genre"],data["Rotten Tomatoes %"],normalize="index").round(3)
print(crosstab_1_percent)
#This normalized crosstab shows the proportion of each genre within evrry rotten tomatoe score value. We use normalize index to tell pandas to convert the counts into proportions(percentages) within each row. 



#b. 2
crosstab_2_percent=pd.crosstab(data["Audience score %"],data["Profitability"],normalize="columns").round(3)
print(crosstab_2_percent)
#This normalized crosstab shows how the audience scores affect the profitability. We use normalize columns so that each column sumns up to 1. 


#b. 3
crosstab_3_percent=pd.crosstab(data["Lead Studio"],data["Year"],normalize=True).round(3)
print(crosstab_3_percent)
#This normalized crosstab shows how many movies each lead studio come out per year. We use normalized true which makes the entire table sum up to 1(100%)


#c) Three way frequency 
#We are using Genre, Lead Studio, and Year 
threeway=pd.crosstab([data["Genre"],data['Lead Studio']],data["Year"])
print(threeway)
#This three way crosstab combines genre, lead studio and year to see how studio activity and genre changed over time. 

import seaborn as sns

#6 
#6.1 a)
sns.relplot(data=data,x="Rotten Tomatoes %",y="Audience score %",col="Genre",kind="scatter")

#6.1 b)
sns.relplot(data=data,x="Rotten Tomatoes %",y="Profitability",hue="Genre",size="Audience score %",col="Lead Studio",kind="scatter")

#6.1 c)
sns.relplot(data=data,x="Year",y="Profitability",kind="line",hue="Genre")
#This line plot shows the year on the x-axis which is a continuous time variable, which shows how average profitability changes over time for each genre.

#6.1 d)
sns.relplot(data=data,x="Year",y="Profitability",kind="line",hue="Genre",errorbar="sd")

#6.1 e)
sns.relplot(data=data,x="Rotten Tomatoes %",y="Profitability",kind="line",hue="Genre",estimator="mean",errorbar="sd")












