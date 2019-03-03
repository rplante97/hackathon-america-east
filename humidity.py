import plotly.plotly as py
import plotly.graph_objs as go
from plotly import tools

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


temp = go.Scatter(
    x=df['Time'],
    y=df['Temperature'],
    name='Temperature (C)'
    )

humidity = go.Scatter(
    x=df['Time'],
    y=df['Humidity'],
    name='Relative Humidity (%)'
    )
soil = go.Scatter(
    x=df['Time'],
    y=df['Soil Moisture'],
    name='Soil Moisture (%)'
    )

light = go.Scatter(
    x=df['Time'],
    y=df['Light Level'],
    name='Light Level'
    )


fig = tools.make_subplots(rows = 2, cols=2, subplot_titles= ('Temperature vs Time','Relative Humidity vs Time', 'Soil Moisture vs Time', 'Light Levels vs Time'))
fig.append_trace(temp, 1, 1)
fig.append_trace(humidity, 1, 2)
fig.append_trace(soil, 2, 1)
fig.append_trace(light, 2, 2)

fig['layout']['xaxis1'].update(title = 'Time')
fig['layout']['xaxis2'].update(title = 'Time')
fig['layout']['xaxis3'].update(title = 'Time')
fig['layout']['xaxis4'].update(title = 'Time')

fig['layout']['yaxis1'].update(title = 'Temperature (C)')
fig['layout']['yaxis2'].update(title = 'Relative Humidity (%)')
fig['layout']['yaxis3'].update(title = 'Soil Moisture (%)')
fig['layout']['yaxis4'].update(title = 'Light Level')


fig['layout'].update(title = 'Greenhouse Data')


#fig = go.Figure(data=data, layout=layout)
py.iplot(fig)

