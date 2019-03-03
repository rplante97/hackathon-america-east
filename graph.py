import plotly.plotly as py
import plotly.graph_objs as go

import MySQLdb
import pandas as pd
import time
from datetime import datetime as dt

def convert_to_datetime(num):
    num = (num * increment_time) + start_time
    num = dt.fromtimestamp(num)
    return num


#Connect to SQL database
db_conn = MySQLdb.connect(host="localhost", user="pi", passwd="password", db="environment_data")
cursor = db_conn.cursor()
cursor.execute('select * from demo_data');

rows = cursor.fetchall()
str(rows)

#Dataframe stuff
df = pd.DataFrame([[ij for ij in i] for i in rows])
#Give each database column a name
df.rename(columns={0: 'Time', 1: 'Temperature', 2: 'Humidity', 3: 'Soil Moisture', 4: 'Light Level'}, inplace=True)

#Convert time column to proper datetime format
start_time = 1532361000
increment_time = 600 #Data was collected every 10 minutes
df['Time'] = df['Time'].apply(convert_to_datetime)


trace1 = go.Scatter(
    x=df['Time'],
    y=df['Temperature']
    )

data = [trace1]
py.iplot(data)

