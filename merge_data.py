import pandas as pd
import numpy as np

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
print(df_all_data)

##parse data to get actual date

dates = []
for time in df_all_data['summary']:
    print(time.split("at")[0])
print(dates)
