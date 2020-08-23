# Covid-19

A different look at US covid data provided by Johns Hopkins.

Sources:
1. https://github.com/CSSEGISandData/COVID-19/blob/master/csse_covid_19_data/csse_covid_19_daily_reports
2. https://www2.census.gov/library/publications/2011/compendia/usa-counties/excel/LND01.xls

* For land area, use column L in the excel file and convert to km if need be.


TODO:
1. Collect latest data from github, save into csv, use text to columns by comma in csv
2. Read both csv with pandas and create master dataframe with active cases per km calculation (new column)