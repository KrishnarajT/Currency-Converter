import requests, json, os, urllib
import PIL, os
from datetime import date, timedelta, datetime
import pandas as pd
import matplotlib.pyplot as plt

def query_all_data():
    """
    Returns a pandas DataFrame that has all the Currencies and
    Their FX values for the past week sorted by date.
    """
    
    they_havent_uploaded = False
    
    with open(os.path.join(os.getcwd(), "My_API_KEY"), 'r') as file:
        my_api_key = file.read()
    
    todays_date = date.today()
    yesterdays_date = todays_date + timedelta(days = -1)
    currency_database = pd.DataFrame()
    # check if the file already exists, if so then dont query again. 
    if os.path.exists(os.path.join(os.getcwd(), 'data', f'{todays_date} currency_database.csv')):
        print('found existing database -------------------------------------------------------------------------------------------------------')
        currency_database = pd.read_csv(os.path.join(os.getcwd(), 'data', f'{todays_date} currency_database.csv'), index_col = 0)
        updated_dates = [datetime.strptime(i, "%Y-%m-%d") for i in currency_database['date'].values]
        currency_database['date'] = updated_dates    
        return currency_database
    elif os.path.exists(os.path.join(os.getcwd(), 'data', f'{yesterdays_date} currency_database.csv')):
        print('found existing database -------------------------------------------------------------------------------------------------------')
        currency_database = pd.read_csv(os.path.join(os.getcwd(), 'data', f'{todays_date} currency_database.csv'), index_col = 0)
        updated_dates = [datetime.strptime(i, "%Y-%m-%d") for i in currency_database['date'].values]
        currency_database['date'] = updated_dates    
        return currency_database
        
    # Checking if the API uploaded todays FX rates, and deciding the start data depending on that. 
    r = requests.get(f'http://api.exchangeratesapi.io/v1/{todays_date}?access_key={my_api_key}')
    if r.status_code != 200:
        print('They havent uploaded')
        they_havent_uploaded = True
        start_date = todays_date + timedelta(days = -1)
    else:
        they_havent_uploaded = False
        start_date = todays_date

    for i in range(7):
        r = requests.get(f'http://api.exchangeratesapi.io/v1/{start_date}?access_key={my_api_key}')
        if r.status_code == 200:
            base_currency = r.json()['base']        
        
            with open('data.json', 'w') as f:
                f.write(r.text)
        
            temp_database = pd.read_json('data.json')
            temp_database.drop(columns=
                ['success', 'timestamp', 'historical', 'base'],
            inplace = True)
            time_delta_day = timedelta(days=-1)
            start_date = start_date + time_delta_day
            currency_database = currency_database.append(temp_database)
        else: print("there was an error retrieving data.")
        
    currency_database.to_csv(os.path.join(os.getcwd(), 'data', f'{todays_date} currency_database.csv'))
    return currency_database    
          
def convert_currency(cur1, cur2, database):
    """
    Arguements: cur1 and cur2 in symbolic format
    database that only has all symbols and values for one date. 
    Returns: how many cur2 is 1 cur1
    """
    
    # these are values from EUR to the respective currencies
    base_cur1_value = database.loc[cur1]['rates'] # Say INR for eg
    base_cur2_value = database.loc[cur2]['rates'] # Say QAR for eg
    
    # this is how much QAR is 1 INR 
    # or how much cur2 is 1 cur1
    converted_val = (1/base_cur1_value) * base_cur2_value
    return converted_val
    
def make_weekly_chart(cur1, cur2, currency_database):
    weekly_data = []
    weekly_date = []
    _date = gen_latest_currency_database(currency_database)['date'][0].date()
    time_delta_date = timedelta(days = -1)
    for i in range(7):
        weekly_date.append(_date.day)
        latest_currency_database = currency_database[currency_database['date'] == _date.isoformat()]
        _date = _date + time_delta_date
        weekly_data.append(convert_currency(cur1, cur2, latest_currency_database))
    plt.style.use('ggplot')
    plt.figure(figsize = (10, 6))
    plt.xlabel('Weekdays')
    plt.ylabel('Value')
    plt.plot(weekly_date, weekly_data, linewidth = 1.5, marker = 'o')
    # plt.title(f'Value of {cur1} to {cur2} in the Past Week')
    plt.savefig(os.path.join(os.getcwd(), "images", f'{cur1} to {cur2} in the past Week.png'), dpi=300)
    
def gen_latest_currency_database(currency_database):
    dates = [i for i in list(currency_database.loc['USD']['date'])]
    dates.sort()
    latest_date = dates[-1]
    print(type(currency_database['date']))
    latest_currency_database = currency_database[currency_database['date'] == latest_date.date().isoformat()]
    return latest_currency_database

def gen_decade_graph(currency_1, currency_2):
    currency_database = pd.read_csv(os.path.join(os.getcwd(), 'data', f'past23yearsdata.csv'), index_col = 0)
    updated_dates = [datetime.strptime(i, "%Y-%m-%d") for i in currency_database['date'].values]
    currency_database['date'] = updated_dates 
    
    # getting the unique dates in the entire database
    dates = currency_database['date'].drop_duplicates(inplace = False)

    currency_vals = []
    dates_vals = []
    for i in dates:
        database = currency_database[currency_database['date'] == i]
        try: 
            currency_vals.append(convert_currency(currency_1, currency_2, database))
            dates_vals.append(i)
        except: 
            print('Currency for this year not found')
    plt.style.use('ggplot')
    plt.figure(figsize = (10, 6))
    plt.xlabel('Years')
    plt.ylabel('Value')
    plt.plot(dates_vals, currency_vals, linewidth = 1.5, marker = '.', color = 'purple')
    # plt.title(f'Value of {cur1} to {cur2} in the Past Week')
    plt.savefig(os.path.join(os.getcwd(), "images", f'{currency_1} to {currency_2} 1999 - 2020.png'), dpi=300)
