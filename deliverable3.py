print("deliverable 3")
import pandas as pd
import seaborn as sns

data = pd.read_csv("movies.csv")

num_cols = ["Audience score %", "Profitability", "Rotten Tomatoes %", "Worldwide Gross", "Year"]
cat_cols = ["Film", "Genre", "Lead Studio"]

#2 Preliminary steps
#a)
top_5_rotten_tomato_score = data.sort_values("Rotten Tomatoes %", ascending=False).head(5)
print("Top 5 rotten tomatoes scores:")
print(top_5_rotten_tomato_score)

top_5_audience_score = data.sort_values("Audience score %", ascending=False).head(5)
print("Top 5 audience scores:")
print(top_5_audience_score)
#showing top 5 values of worldwide gross and audience score within dataset, code sorts audeince score values in descending order then prints the first 5 which are the 5 largest values.

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
print("Initial null values inspection:", data.isnull().sum())
#checks how many missing values are in each column
#using methods b and c since dataset is small
#numerical values
data[num_cols] = data[num_cols].fillna(data[num_cols].mean())

#categorical columns
data[cat_cols] = data[cat_cols].fillna("Unknown")

print("Final null values inspection:", data.isnull().sum())
#split numerical and categorical columns into their own variables to be easily accessible. The numerical null values were replaced with the mean of the column. The categorical null values were replaced with UNKNOWN. An initial null values inspection was done to check how many null values there were before correcting them. A second inspection was done after the correction to assure the correction took care of all the null values.
#since the data set is small rather than removing rows with missing values their values were inputted using the mean for numerical columns to maintain a reasonable size for the data set. If the column did not have numerical values then "Unknown" was inputted into the cell.

#d
data["Worldwide Gross"] = data["Worldwide Gross"].str.replace("$", "", regex=False)
#This code eliminates the dollar sign in all the cells of the column "Worldwide Gross" so that the values can be treated numerically rather than as strings. The function replace was used and replaced every dollar sign to nothing. Regex=False was included because the pandas module automatically assumes regex=True meaning it will treat the value as a regular expression. The $ is an expression used to end a string by writing regex=False it will consider the dollar sign to be a regular symbol with no specific meaning.

#3 Univariate non-graphical EDA
num_cols = ["Audience score %", "Profitability", "Rotten Tomatoes %", "Worldwide Gross", "Year"]
#numerical columns
#created a variable to access only the numerical columns and then created a loop so each statistical value can be printed
#mean: average value using the mean function
#median: middle value of the column thats been sorted in ascending or descending order using sorting and median functions
#mode: most repeated value using mode function
#standard deviation: amount of variation in the dataset relative to the mean using the standard deviation function
#variance: how spread out the data is in relation to its mean using the variance function
#skewness: measuring if the data is leans to one side  using the skew function
#kurtosis: measuring how many present the outliers are using the kurtosis function
#quartiles: values of which 25%, 50%, and 75% of the data lays, using the quantile function

#for x in num_cols:
#    if x in data:
#        print("Mean:", data[x].mean())
#        print("Median:", data[x].median())
#        print("Mode:", data[x].mode().values)
#        print("Standard deviation:", data[x].std())
#        print("Variance:", data[x].var())
#        print("Skewness:", data[x].skew())
#        print("Kurtosis", data[x].kurt())
#        print("Quartiles 25%, 50% and 75%:", data[x].quantile([0.25, 0.5, 0.75]))

cat_cols = ["Film", "Genre", "Lead Studio"]
#categorical columns
#non numerical columns
#frequency counts: counts the amount of times a string occurs in a column of data
#proportion: takes the frequency count and uses normalize to convert it to a proportion rather than a count so the frequency is relative to the number of items in the column.
#mode: finds the item most repeated throughout the column and the number of unique categories in that column
#for x in cat_cols:
#    if x in data:
#        print("Frequency counts:", data[x].value_counts())
#        print("Proportion:", data[x].value_counts(normalize=True))
#        print("Mode:", data[x].mode().values)
#        print("Unique values:", data[x].nunique())


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
#a) 3 times with different variables 
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


#b)Using proportions or percentages 

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


#c)Three way frequency table
#We are using Genre, Lead Studio, and Year 
threeway=pd.crosstab([data["Genre"],data['Lead Studio']],data["Year"])
print(threeway)
#This three way crosstab combines genre, lead studio and year to see how studio activity and genre changed over time. 


#6 Multivariate graphical EDA
#6.1 a) Faceting feature 
sns.relplot(data=data,x="Rotten Tomatoes %",y="Audience score %",col="Genre",kind="scatter")
#This plot shows the relationship between rotten tomatoes % and audience score % across different genres. Each represents a specific genre, which helps visualize whether critical and audience ratings tend to align more strongly in certain genres than others.

#6.1 b) Plot representing 5 variables at once
sns.relplot(data=data,x="Rotten Tomatoes %",y="Profitability",hue="Genre",size="Audience score %",col="Lead Studio",kind="scatter")
#This scatter plot  visualizes 5 variables: Rotten tomatoes, profitability, genre, audience score and lead studios. Each subplot represents a lead studio, with the x-axis showing rotten tomatoes and the y-axis showing profitability. The color of eahc point indicates the genre, and the size of each point represents the audience score. 

#6.1 c) Line plot
sns.relplot(data=data,x="Year",y="Profitability",kind="line",hue="Genre")
#This line plot shows how the average profitability of movies changed over time for each genre. The x-axis represents the year, while the y-axis represents the profitability. Each colored line corresponds to a genre, allowing us to observe which genres were more or less profitable during the years 2007-2011. The x-axis which is a continuous time variable, which shows how average profitability changes over time for each genre.

#6.1 d) Standard deviation
sns.relplot(data=data,x="Year",y="Profitability",kind="line",hue="Genre",errorbar="sd")
#This plot shows the average profitability over time for each genre, with shaded areas representing the standard deviation. The shaded regions illustrate the variation of profitability among movies within each genre. A wider shaded area means that the profitability values were more spread out, while narrower area means the values are more stable. This helps identify which genres had more fluctuating probability between the years 2007 and 2011.

#6.1 e) Linear regression 
sns.relplot(data=data,x="Rotten Tomatoes %",y="Profitability",kind="line",hue="Genre",estimator="mean",errorbar="sd")
#This plot shows the relationship between rotten tomatoes ratings and profitability for different genres.The lines represent the average profitability for each rotten tomatoe score. We can observe how profitability tends to change as critic scores increase.

#6.2 Visualizing categorical data
#6.2 a) Scatter plot with jitter enabled
sns.catplot(data=data,x="Genre",y="Profitability",kind="strip",jitter=True)
#This shows the profitability of movies for each genre, using jitter to prevent overlapping points. Enabling jitter spreads the data slightly along the x-axis, making it easier to distinguish individual movies with similar profitability values. It helps visualize how profitability varies among different genres while ensuring that dense areas of data are easier to intepret.

#6.2 b) Scatter plot with jitter disabled 
sns.catplot(data=data,x="Genre",y="Profitability",kind="strip",jitter=False)
#This plot shows the profitability of movies across different genres, with jitter disabled. Disabling jitter stacks the points vertically, making it easier to see where multiple movies share the same profitability values. Genre was chosen on the x-axis because it allows comparisons between categories, and profitability on the y-axis because it is continuous, helping visualize which genres tend to produce more profitable movies.


#6.2 c) "beeswarm" plot representing 3 variables 
sns.catplot(data=data,x="Genre",y="Profitability",hue="Lead Studio",kind="swarm")
#This shows the profitability of movies across different genres and lead studios. Each point represents a studio, with colors identifying which studio. We can see that comedy and romance genres have the widest spread which means their profitability varies more compared to others. 

#6.2 d) Box plot representing 3 variables 
sns.catplot(data=data,x="Genre",y="Profitability",hue="Lead Studio",kind="box")
#The box plot shows the distribution of profitability across different movie genres and lead studios. Each colored box represents a studio.

#6.2 e) use boxenplot()
sns.catplot(data=data,x="Genre",y="Profitability",kind="boxen")
#This plot shows the shape of the profitability distribution for each movie genre. The boxenplot shows the quantile layers, giving more detailed view. We can see that comedy and romance genres have higher variation in profitability, while fantasy and action have smaller range. 

#6.2 f) Split violin plot representing 3 variables with bandwidth adjusted 
sns.catplot(data=data,x="Genre",y="Profitability",hue="Lead Studio",kind="violin",bw=1)
#This plot represents the distribution of profitability across genres and studios. The bandwidth was adjusted to smooth the shapes and make differences between studios clearer.

#6.2 g) Violin plot with scatter points 
sns.catplot(data=data,x="Genre",y="Profitability",kind="violin",inner="point")
#The violin plot displays the distribution of profitability across different genres.The shape of the violin indicates how profitability values are spread within each genre, showing where the most data points are concentrated. Drama and comedy show wider distributions, while animation and action have smaller ranges.

#6.2 h) Bar plot representing 3 variables shpwing 97% confidence intervals 
sns.catplot(data=data,x="Genre",y="Profitability",hue="Lead Studio",kind="bar",ci=97)
#This bar plot shows the average profitability by genre and lead studio with 97% confidence intervals. This shows which studios tend to produce more profitable films within each genre.

#6.2 i) Point plot representing 3 variables showing 90% confidence intervals 
sns.catplot(data=data,x="Genre",y="Profitability",hue="Lead Studio",kind="point",ci=90,linestyle="--")
#This plot displays the average profitability of each lead studio across different genres, with 90% confidence intervals.Each color represents a different studio and the dashed lines connect profitability trends across genres.

#6.2 j) Bar plot 
sns.catplot(data=data,x="Genre",kind="count")
#This bar plot shows the number of movies in each genre. Comedy has the highest number of movies in the dataset,followed by romance and drama. Genres like animation, fantasy, and action appear less frequently. 