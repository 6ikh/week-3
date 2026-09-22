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

url = 'https://github.com/melaniewalsh/Intro-Cultural-Analytics/raw/master/book/data/bellevue_almshouse_modified.csv'
df_bellevue = pd.read_csv(url)

def task_1():
    df = df_bellevue.copy()
    df['gender'] = df['gender'].replace('u',pd.NA)
    return df.isna().sum().sort_values(ascending=True).index.tolist()

def task_2():
    df = df_bellevue.copy()
    df['date_in'] = pd.to_datetime(df['date_in'])
    df['year'] = df['date_in'].dt.year
    return df.groupby('year').size().reset_index(name='total_admissions')

def task_3():
    return df_bellevue.groupby('gender')['age'].mean()

def task_4():
    return df_bellevue['profession'].value_counts().head(5).index.tolist()
