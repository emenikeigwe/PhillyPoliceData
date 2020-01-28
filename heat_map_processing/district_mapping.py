import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import re, datetime
import matplotlib.pyplot as plt



csv1= 'policedata/ppd_complaints.csv'
csv2 = 'policedata/ppd_complainant_demographics.csv'
csv3 = 'policedata/ppd_complaint_disciplines.csv'
csv4 = 'policedata/Boundaries_District.csv'


##preparing csvs into data frames
#complaint data
df_complaints = pd.read_csv(csv1)
#boundaries_district
df_police = pd.read_csv(csv4)
#drop police districts 23, Other Jurisdiction, and 4 that do not appear in current police district
df_complaints = df_complaints[df_complaints['district_occurrence'] != "400"]
df_complaints = df_complaints[df_complaints['district_occurrence'] != "2300"] 
df_complaints = df_complaints[df_complaints['district_occurrence'] != "Other Jurisdiction"]
df_complaints = df_complaints.dropna()
df_complaints['district_occurrence'][df_complaints['district_occurrence'] == "9"] = "900" #have lone case of 9 put into district "900"
df_complaints['district_occurrence'] = pd.to_numeric(df_complaints['district_occurrence'])

#clean to get district names without "00" at e d 
df_complaints['district_occurrence']= df_complaints['district_occurrence'] / 100
#make value count into dataframe
val_count = df_complaints['district_occurrence'].value_counts()
df_heat_map =  val_count.rename_axis('DISTRICT_').reset_index(name='counts')
#export dataframe to dsv
df_heat_map.to_csv('heat_map_data.csv')

