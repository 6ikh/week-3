import seaborn as sns
import pandas as pd

# update/add code below ...

# defining the fibonacci function with n as a parameter
def fibonacci(n):
    """Return the nth Fibonacci number"""
    # if n is less than or equal to 0, return 0
    if n <= 0:
        return 0
    # else if n is equal to 1, return 1
    elif n == 1:
        return 1
    # else if the number is greater than 1
    else:
        # recursively call the fibonacci function and return the sum
        return fibonacci(n - 1) + fibonacci(n - 2)

# declaring function to_binary with n as a parameter
def to_binary(n):
    """Convert an integer number to binary"""
    # if number is less than 2
    if n < 2:
        # return the string representation of n
        return str(n)
    # else, if number is greater than or equal to 2
    else:
        # recursively divide n by 2 add each remainder to n
        return to_binary(n // 2) + str(n % 2)

#loading in the data set by url
url = 'https://github.com/melaniewalsh/Intro-Cultural-Analytics/raw/master/book/data/bellevue_almshouse_modified.csv'
# loading the data set into a pandas dataframe
df_bellevue = pd.read_csv(url)

# function task_1
def task_1():
    df = df_bellevue.copy()
    df['gender'] = df['gender'].replace("?","g","h",pd.NA)
    missing = df.isna().sum()
    return missing.sort_values(ascending=True).index.sort_values().tolist()

# function task_2
def task_2():
    """Return the total number of admissions by year in the Bellevue dataset"""
    # create a copy of the dataset
    df = df_bellevue.copy()
    # convert the date_in column to datetime format
    df['date_in'] = pd.to_datetime(df['date_in'])
    # create new column called year by extracting the year from date_in column
    df['year'] = df['date_in'].dt.year
    # group df by year and count the number of admissions & reset the index
    return df.groupby('year').size().reset_index(name='total_admissions')

# function task_3
def task_3():
    """Return the average age of patients by gender in the Bellevue dataset"""
    # group by the gender and the age to return the mean
    return df_bellevue.groupby('gender')['age'].mean()

# function task_4
def task_4():
    """Return the top 5 professions in the Bellevue dataset"""
    # take value counts of the profession column and return the top 5 professions
    return df_bellevue['profession'].value_counts().head(5).index.tolist()
