import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import re, datetime
import matplotlib.pyplot as plt



csv1= 'policedata/ppd_complaints.csv'
csv2 = 'policedata/ppd_complainant_demographics.csv'
csv3 = 'policedata/ppd_complaint_disciplines.csv'
philly_race_csv = 'philly_census/Philly_General_ACS2018.csv'


##preparing csvs into data frames
#complaint data
df_complaints = pd.read_csv(csv1)

#dem of complaint data
df_dem = pd.read_csv(csv2)
#merge data
df_merge_race = df_complaints.merge(df_dem)
#instead of null type create "None" for reports of unrecorded reports
df_merge_race = df_merge_race.applymap(str)
df_merge_race['complainant_race'][df_merge_race['complainant_race'] == "nan"] = "None"

#philly race census data then getting one race data
df_philly_race = pd.read_csv(philly_race_csv)
df_philly_race.columns = df_philly_race.iloc[0]
df_philly_race = df_philly_race.filter(regex = "Percent Estimate!!HISPANIC OR LATINO AND RACE!!")
del df_philly_race['Percent Estimate!!HISPANIC OR LATINO AND RACE!!Total population']
#regex to clean column names
df_philly_race = df_philly_race.rename(columns=lambda nam: nam.split("population!!")[1])
df_philly_race = df_philly_race.drop(df_philly_race.index[0])
df_philly_race = df_philly_race.apply(pd.to_numeric)

# #bar graph with race as bins and the number of counts for raw count
X = np.array(df_merge_race['complainant_race'].unique()) #
Y = df_merge_race['complainant_race'].value_counts()
plt.bar(X, Y)
plt.title("Raw Number of Reports by Race")
plt.xlabel("Race")
plt.ylabel("Number of Reports")
plt.show()

# #bar graph wtih raw race as percentage
X = np.array(df_merge_race['complainant_race'].unique()) #
Y = df_merge_race['complainant_race'].value_counts() / df_merge_race['complainant_race'].value_counts().sum() * 100
plt.bar(X, Y)
plt.title("Raw Percentage of Reports by Race")
plt.xlabel("Race")
plt.ylabel("Percent")
plt.show()

# #bar graph wtih raw race as percentage with 
# #middle east & multi ethnic as a part of Other
# #indian part of Asian
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


##bar graph with race percentages overall based on ACS 2018 Philadelphia demographics
##middle east & multi ethnic as a part of Other
#indian part of Asian
df_merge_race['complainant_race'][df_merge_race['complainant_race'] == "indian"] = "asian"
df_merge_race['complainant_race'][df_merge_race['complainant_race'] == "middle east"] = "other"
df_merge_race['complainant_race'][df_merge_race['complainant_race'] == "multi ethnic"] = "other"
X = np.array(df_merge_race['complainant_race'].unique()) 
Y_police_complaints = df_merge_race['complainant_race'].value_counts() / df_merge_race['complainant_race'].value_counts().sum() * 100
#taking philly race data and applying to races from police data
Y_philly_race = np.array(list([df_philly_race.iloc[0]['Not Hispanic or Latino!!Black or African American alone'], df_philly_race.iloc[0]['Not Hispanic or Latino!!White alone'],\
     0, df_philly_race.iloc[0]['Hispanic or Latino (of any race)'], df_philly_race.iloc[0]['Not Hispanic or Latino!!Asian alone'], \
    df_philly_race.iloc[0]['Not Hispanic or Latino!!Native Hawaiian and Other Pacific Islander alone'] + df_philly_race.iloc[0]['Not Hispanic or Latino!!Two or more races']]))
bar_width = 0.35
indx = np.arange(len(X))
fig, ax = plt.subplots()
barPolice = ax.bar(indx - bar_width/2, Y_police_complaints, bar_width, label='Police Complaints')
barPhilly = ax.bar(indx + bar_width/2, Y_philly_race, bar_width, label='Philadelphia City ACS 2018')
ax.set_xticks(indx)
ax.set_xticklabels(X)
ax.set_xlabel("Race")
ax.set_ylabel("Percentage")
ax.set_title("Demographics of Philadelphia Police Complaints \n Compared to Philadelphia City")
ax.legend()
plt.show()


