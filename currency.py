import requests, json, os, urllib
import PIL
from datetime import date, timedelta
import pandas as pd

def query_all_data():
    # """
    # Returns a pandas DataFrame that has all the Currencies and
    # Their FX values for the past week sorted by date.
    # """
    # with open(os.path.join(os.getcwd(), "My_API_KEY"), 'r') as file:
    #     my_api_key = file.read()
    
    # todays_date = date.today() - timedelta(days=+1)
    # currency_database = pd.DataFrame()
    # for i in range(7):
    #     r = requests.get(f'http://api.exchangeratesapi.io/v1/{todays_date}?access_key={my_api_key}')
    #     if r.status_code == 200:
    #         base_currency = r.json()['base']        
        
    #         with open('data.json', 'w') as f:
    #             f.write(r.text)
        
    #         temp_database = pd.read_json('data.json')
    #         temp_database.drop(columns=
    #             ['success', 'timestamp', 'historical', 'base'],
    #         inplace = True)
    #         time_delta_day = timedelta(days=-1)
    #         todays_date = todays_date + time_delta_day
            
    #         currency_database = currency_database.append(temp_database)
    #     else: 
    #         print('There is an Error in retrieving data using the API')
    #         print(r.json())
    #         return 0
    currency_database = pd.read_csv('currency_database.csv', index_col = 0)
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
    
def make_weekly_chart(cur1, cur2, currency_datebase):
    weekly_data = []
    weekly_date = []
    date = date.today()
    time_delta_date = timedelta(days = -1)
    for i in range(7):
        latest_currency_database = currency_database[currency_database['date'] == date.isoformat()]
        date = date + time_delta_date
        weekly_data.append(convert_currency(cur1, cur2, latest_currency_database))
        weekly_date.append(date.day)
    plt.style.use('ggplot')
    plt.figure(figsize = (10, 7))
    plt.xlabel('Weekdays')
    plt.ylabel('Value')
    plt.title('Value of {cur1} to {cur2} in the Past Week')
    plt.plot(weekly_date, weekly_data, linewidth = 1.5)
    plt.savefig('sth.png', dpi=300)
    
    