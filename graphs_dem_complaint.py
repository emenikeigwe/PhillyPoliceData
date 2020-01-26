import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import re, datetime
import matplotlib.pyplot as plt



csv1= 'policedata/ppd_complaints.csv'
csv2 = 'policedata/ppd_complainant_demographics.csv'
csv3 = 'policedata/ppd_complaint_disciplines.csv'

#complaint data
df_complaints = pd.read_csv(csv1)

#dem of complaint data
df_dem = pd.read_csv(csv2)
#merge data
df_merge_race = df_complaints.merge(df_dem)
#instead of null type create "None" for reports of unrecorded reports
df_merge_race = df_merge_race.applymap(str)
df_merge_race['complainant_race'][df_merge_race['complainant_race'] == "nan"] = "None"
print(df_merge_race['complainant_race'].value_counts().sum())

#bar graph with race as bins and the number of counts for raw count
X = np.array(df_merge_race['complainant_race'].unique()) #
Y = df_merge_race['complainant_race'].value_counts()
plt.bar(X, Y)
plt.title("Raw Number of Reports by Race")
plt.xlabel("Race")
plt.ylabel("Number of Reports")
plt.show()

#bar graph wtih raw race as percentage
X = np.array(df_merge_race['complainant_race'].unique()) #
Y = df_merge_race['complainant_race'].value_counts() / df_merge_race['complainant_race'].value_counts().sum() * 100
plt.bar(X, Y)
plt.title("Raw Percentage of Reports by Race")
plt.xlabel("Race")
plt.ylabel("Percent")
plt.show()

#bar graph wtih raw race as percentage with 
#middle east & multi ethnic as a part of Other
#indian part of Asian
df_merge_race['complainant_race'][df_merge_race['complainant_race'] == "indian"] = "asian"
df_merge_race['complainant_race'][df_merge_race['complainant_race'] == "middle east"] = "other"
df_merge_race['complainant_race'][df_merge_race['complainant_race'] == "multi ethnic"] = "other"
X = np.array(df_merge_race['complainant_race'].unique()) 
Y = df_merge_race['complainant_race'].value_counts() / df_merge_race['complainant_race'].value_counts().sum() * 100
plt.bar(X, Y)
plt.title("Percentage of Reports by Race")
plt.xlabel("Race")
plt.ylabel("Percent")
plt.show()