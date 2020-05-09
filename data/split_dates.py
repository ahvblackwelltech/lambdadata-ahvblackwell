# Function to split dates ("MM/DD/YYYY", etc.) into multiple columns
import pandas as pd
import numpy as np


date = pd.to_datetime(input("Today's Date Is: "))
date_series = date + pd.to_timedelta(np.arange(12), 'D')



# Creating DataFrame
def splitDates(date):
    assert date_series

    df = pd.DataFrame()
    df['date'] = date_series

    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month
    df['day'] = df['date'].dt.day
    df['hour'] = df['date'].dt.hour
    df['minute'] = df['date'].dt.minute

    df.index = df.date

    splitDates()
   
