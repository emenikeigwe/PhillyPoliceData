import pandas as pd
import numpy as np
import re, datetime

csv1= 'policedata/ppd_complaints.csv'
csv2 = 'policedata/ppd_complainant_demographics.csv'
csv3 = 'policedata/ppd_complaint_disciplines.csv'

#complaint data
df_complaints = pd.read_csv(csv1)

#outcome of complaint data
df_outcome = pd.read_csv(csv2)

#complaint demographic data
df_dem = pd.read_csv(csv3)
#comebine two csvs
df_merge1 = df_complaints.merge(df_outcome)
#combine three csvs
df_all_data = df_merge1.merge(df_dem)
#print(df_all_data)

##parse data to get actual date

dates = []
date_format = r"(\d{1,2}-\d{1,2}-\d{2,4})"
df_all_data['complaint_date'] = df_all_data['summary'].str.extract(date_format)

test_string = "sdsfsd"
# get place
indexNames = df_all_data[df_all_data['complaint_date'].isnull()].index
df_all_data.drop(indexNames, inplace=True)
print(df_all_data.iloc[90]['complaint_date'])
df_all_data['complaint_date'] = pd.to_datetime(df_all_data['complaint_date'], errors="ignore")
test_type = type(df_all_data.iloc[81]['complaint_date'])
print(df_all_data['complaint_date'][type(df_all_data['complaint_date']) == type(test_string)].index)

#print(df_all_data[type(df_all_data['complaint_date']) == type(test_string)].index)
# print(df_all_data.iloc[5491]['summary'])

# for r in df_all_data['complaint_date']:
#     print(type(r))

#df_all_data.to_csv('cleaned_police_data.csv')
# 