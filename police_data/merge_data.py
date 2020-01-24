import pandas as pd
import numpy as np

url1 = 'ppd_complaints.csv'
url2 = 'https://phl.carto.com/api/v2/sql?q=SELECT+*+FROM+ppd_complaint_disciplines&filename=ppd_complaint_disciplines&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator'
url3 = 'https://phl.carto.com/api/v2/sql?q=SELECT+*+FROM+ppd_complainant_demographics&filename=ppd_complainant_demographics&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator'

#complaint data
df_complaints = pd.read_csv(url1)
print(df_complaints.columns)
df_complaints.head()

# #outcome of complaint data
# df_outcome = pd.read_csv(url2)
# print(df_outcomes.columns)
# df_outcomes.head()

#complaint demographic data
# df_dem = pd.read_csv(url3)
# print(df_dem.columns)
# df_dem.head()