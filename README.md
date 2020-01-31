# PhillyPoliceData
Project for Hack the City (11.s188) by Ahmed, Amelia, and Arlene analyzing connections between police complaints in Philadelphia, race, geographic data, and other treatments. The CAP Data was taken from [Open Data Philly](https://www.opendataphilly.org/dataset/police-complaints/resource/7f7d472f-c49c-4364-b6e0-3a079e6b7d7f), demographic data from the city came from the Census American Community Survey 2018, and the Police District Data for the heatmap was also taken from [Open Data Philly](https://www.opendataphilly.org/dataset/police-districts). 

## Directories and file locations
/graphs/ contains images of graphs and other visual outputs and Tableau files

/heat_map_processing/ includes code and output csv used in Carto to compile heatmap also includes link to Carto map

/outputdata/ contains processed dataframes created through other code and fed into Tableau and other graphing applications

/philly_census/ contains the CSVs for the demographics of Philadelphia from the 2018 US Census

/policedata/ contains the CSVs of basic data regarding complaints against officers, as well as the boundaries of the different police districts

/graphs/ contains the PNGs and Tableau workbooks of created graphs

Ahmed_Notebook.ipnyb contains code to do some basic data processing and counting of the complaints against officers, as well as to aggregate the data into single rows relating individual complaints to their final outcomes.

Boundaries_District.zip are shapefiles for Philly Police District boundaries

cleaned_police_data.csv is an output from merge_data.py from initial data cleaning

graphs_dem_copmlaint.py is code for certain graphs with code for cleaning racial data

merge_data.py contains code to clean data

race_percent.csv includes data output from graphs_dem_complaint.py that was also used in the heat map
