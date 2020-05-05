# NOAA Nighttime Lights
#### Vid Chan, Anderson Monken, Doug Neumann, Nicole Yoder

This repository contains all of our code and visualizations.
Here is a guide for the various files.


## Economic Data
### Getting and cleaning data from four sources (all located in Econ_Data_Sources folder):
#### World Integrated Trade Solution
Initial data: WITS_Export.csv, WITS_Import.csv

Cleaning code: WITS_data.ipynb

Cleaned data: WITS_Clean.csv

#### International Monetary Fund World Economic Outlook Reports
Initial data: WEO_intial.csv

Cleaning code: WEO_data.ipynb

Cleaned data: WEO_Clean.csv

#### World Bank
Initial but later redone code folder: Vid_WB

Initial data and cleaning code: WB_data.ipynb

Cleaned data: WB_Clean.csv

#### Organisation for Economic Co-Operation and Development
Initial data and cleaning code: OECD_data.ipynb

Cleaned data: OECD.csv

### Merging four sources together and some more cleaning:
Code: Merging_Econ_Data.ipynb

Cleaned data: econ_data.csv

## Lights Data
### Getting and cleaning data:
downloading data: light_data_parallel_download.py
processing nightlight data in geopyspark: nightlight_processing.ipynb
 
processed data: lights_data.pkl, lights_data.csv

### Merging with the economic data:
Merging code: Merging_Light_Econ_Data.ipynb

Merged/cleaned data: merged_data.pkl

### Visualizations:
light_EDA.ipynb
output graphs: light.html, light_index.html, light_gdp.html, light_gdp_index.html


### Building models:
Code: models.ipynb


## Presentation
presentation.Rmd, presentation.html

## Report
()()()
