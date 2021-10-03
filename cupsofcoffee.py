import csv 
with open("cups of coffee vs hours of sleep.csv", newline="") as f:
    reader=csv.reader(f)
    file_data=list(reader)

file_data.pop(0)
total_HoursOfSleep=0
total_entries=len(file_data)

for hoursOfSleep in file_data:
    total_HoursOfSleep+=float(hoursOfSleep[1])

mean = total_HoursOfSleep/total_entries
print("mean/average is: "+str(mean))

import pandas as pd
import plotly.express as px

df=pd.read_csv("cups of coffee vs hours of sleep.csv")

fig=px.scatter(df, x="Coffee in ml", y="sleep in hours")
fig.update_layout(shapes=[dict(type="line",y0=mean,y1=mean,x0=0,x1=total_entries)])
fig.update_yaxes(rangemode="tozero")
fig.show()