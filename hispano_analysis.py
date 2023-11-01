import pandas as pd
import re
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

#%%

path = r"C:\Users\Sergio\PycharmProjects\coffe_shop_review_analysis\hispano.csv"
reviews = pd.read_csv(path,encoding= "UTF-8" )

#Creating the regex extraction function

def extract_number_letter(text):
    regex = r"(\d+)\s*(\w+)"
    matches = re.findall(regex, text)
    result = ', '.join([f"{int(num)}, {word[0]}" for num, word in matches])
    return result

#Applying the function to the time column

reviews['time_ext'] = reviews['time'].apply(extract_number_letter)

#Separating the time_ext column into number and year, month or day columns

reviews['number'] = reviews['time_ext'].str.split(",").str.get(0)
reviews['number'] = reviews['number'].str.replace(" ","")
reviews['number'] = reviews['number'].astype(int)
reviews['y_m_w'] = reviews['time_ext'].str.split(",").str.get(1)
reviews['y_m_w'] = reviews['y_m_w'].str.replace(" ","")

#Replacing the "a" for "y" for year and the "s" for "w" for week

reviews['y_m_w'] = reviews['y_m_w'].str.replace("a","y")
reviews['y_m_w'] = reviews['y_m_w'].str.replace("s","w")

#We create a day_factor column according if is year (365), month (30) or week (7) the resulting number of days will be
#substracted form today's date in order to get an approximate review emission date

def get_day_factor(value):
    if value == "y":
        return 365
    elif value == "m":
        return 30
    elif value == "w":
        return 7
    else:
        return None

reviews['day_factor'] = list(map(get_day_factor, reviews['y_m_w']))

#We set todays date

today = datetime.today()

reviews['appx_rev_date'] = [(today - timedelta(days=(row['number'] * row['day_factor']))).date() for _, row in reviews.iterrows()]

#We are droping the columns that are usless from this point and I will only keep the client, review and appx_rev_date

reviews = reviews.drop(columns = ['time','time_ext', 'number', 'y_m_w', 'day_factor'])

reviews.to_csv(r"C:\Users\Sergio\PycharmProjects\coffe_shop_review_analysis\hispano_cleaned.csv")

