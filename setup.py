# setup.py
# Created 20210524 1537 
# Invoke with %run "C:\\setup.py"
# Modified (see version)

VERSION = "20210720 2217 "

import datetime
import humanize
import numpy as np
import os
import pandas as pd
import plotly.express as px
import pyperclip
import re
import sidetable
import snowflake.connector
import time
from snowflake.connector.pandas_tools import write_pandas
from dotenv import load_dotenv

_ = load_dotenv()

# Get non-null counts
pd.options.display.max_info_rows = 16907850

# Connection string
conn = snowflake.connector.connect(
                user=os.getenv('user'),
                password=os.getenv('password'),
                account=os.getenv('account'),
                warehouse=os.getenv('warehouse'),
                database=os.getenv('database'),
                schema=os.getenv('schema')
                )

# Execute a statement that will generate a result set.
cur = conn.cursor()

def compare_sets(list1, list2):
    """Make a count of the intersections of two sets, A and B"""
    set1 = set(list1)
    set2 = set(list2)
    set2_intersection_set1 = set2.intersection(set1)
    result = {'IN A':[len(set1), len(set2_intersection_set1), round(len(set1)/len(set1)*100,1), round(len(set2_intersection_set1)/len(set2)*100,1)]}
    result['IN B'] = [len(set2_intersection_set1), len(set2), round(len(set2_intersection_set1)/len(set1)*100,1), round(len(set2)/len(set2)*100,1)]
    result['NOT IN A'] = [0, len(set2 - set1), 0, round(len(set2 - set1)/len(set2)*100,1)]
    result['NOT IN B'] = [len(set1 - set2), 0, round(len(set1 - set2)/len(set1)*100,1), 0]
    df = pd.DataFrame.from_dict(result, orient='index', columns=['A', 'B', '% of A', '% of B'])
    return df


def d(vars):
    """List of variables starting with string "df" in reverse order. Usage: d(dir())

    @vars list of variables output by dir() command
    """
    list_of_dfs = [item for item in vars if (item.find('df') == 0 and item.find('_') == -1 and item != 'dfs')]
    list_of_dfs.sort(key=lambda x:int(re.sub("[^0-9]", "", x.replace('df',''))) if len(x) > 2 else 0, reverse=True)
    return list_of_dfs


def e(start_time):
    """Return human readable time delta

    @start_time time to compare to current time
    """
    print(f'Time now: {datetime.datetime.now().strftime("%Y-%m-%d %H:%M")}')
    print(f"Time since start: {humanize.naturaldelta(time.monotonic() - start_time)}")


def execute(sql):
    """Execute a SQL command"""
    start_time = time.monotonic()
    _ = cur.execute(sql)
    end_time = time.monotonic()
    elapsed = end_time - start_time
    print(f"Elapsed time {elapsed:.2f}")
    return


def find_col_with(df, char_to_find):
    """Return column index of first column containing char_to_find

    @char_to_find character to search for in column name
    """
    first_column_with_char_to_find = [col for col in df.columns if col.find(char_to_find) > -1][0]
    return list(df.columns).index(first_column_with_char_to_find)


def find_max_order(df, start_col=1):
    """Find the max value in each column and use it to put columns in rank order

    @start_col Index of starting column (typically 1 as first column -- column 0 -- is a date or label)
    """
    return list(df[df.columns[start_col:]].max().sort_values(ascending=False).keys())


def find_percentage_total(df, start_col=1):
    """Find total and percent of total for columns of Pandas dataframe

    @start_col Index of starting column (typically 1 as first column -- column 0 -- is a date or label)
    """
    # Get values for col1,col2 and col3
    total = pd.Series(data=np.zeros(len(df)))
    col_count = len(df.columns)
    for i in range(start_col, col_count):
        total += df.iloc[:,i]
    df.insert(len(df.columns), 'total', total)
    for i in range(start_col, col_count + 1):        
        pct_of_total = round((df.iloc[:,i]/total)*100, 2)

        # Create Pandas DF with new column of pct_of_total
        df.insert(len(df.columns),f"{df.columns[i]} %", pct_of_total)
    
    # Pull original dataframe to show total and %
    return df


def query(sql):
    """Run a SQL query and fetch result into Pandas DataFrame"""
    start_time = time.monotonic()
    _ = cur.execute(sql)
    df = cur.fetch_pandas_all()
    end_time = time.monotonic()
    elapsed = end_time - start_time
    print(f"Elapsed time {elapsed:.2f}")
    return df


def t(title_string):
    """Add "as at {today}" to title. Usage: t(title_sting)

    @title_string text to preceed the "as at" part
    """
    today = datetime.datetime.today().strftime('%d %b %Y')
    title = f"{title_string} as at {today}"
    print(title)
    pyperclip.copy(title)
    print("(now on clipboard)")
    return title


start_time = time.monotonic()
print(f"Setup Complete v {VERSION}")
