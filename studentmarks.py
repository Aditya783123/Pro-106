import csv 
with open("Student Marks vs Days Present.csv", newline="") as f:
    reader=csv.reader(f)
    file_data=list(reader)

file_data.pop(0)
total_DaysPresent=0
total_entries=len(file_data)

for daysPresent in file_data:
    total_DaysPresent+=float(daysPresent[1])

mean = total_DaysPresent/total_entries
print("mean/average is: "+str(mean))

import pandas as pd
import plotly.express as px

df=pd.read_csv("Student Marks vs Days Present.csv")

fig=px.scatter(df, x="Marks In Percentage", y="Days Present")
fig.update_layout(shapes=[dict(type="line",y0=mean,y1=mean,x0=0,x1=total_entries)])
fig.update_yaxes(rangemode="tozero")
fig.show()