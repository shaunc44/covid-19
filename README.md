# Covid-19

A different look at US covid data provided by Johns Hopkins, specifically a calculation of the active Covid cases per square mile (or kilometer),   The NY Times reports Covid growth and decline around America as cases per 100,000 residents, not case per sq mi.  The NYT approach is skewed because a large, sparse county any where in the country could have few people but enough cases to make it appear to be experiencing and outbreak while the number of case per sq mi is very low compared to, say, a borough in NYC that has low cases per 100k residents, but those cases exist in an small, but highly populated area.  Example: Queens County (NY) has fewer cases per capita but signficantly higher cases per sq mi.  Personally, I'd rather be farther away from someone that has Covid than live in a place that has higher covid per capita.

## Sources:
1. https://github.com/CSSEGISandData/COVID-19/blob/master/csse_covid_19_data/csse_covid_19_daily_reports
2. https://www2.census.gov/library/publications/2011/compendia/usa-counties/excel/LND01.xls
3. For Maps: see NY times map and -- https://docs.mapbox.com/api/maps/

## TODO:
1. Collect latest Covid-19 data from github, save into csv and then use text to columns by comma in csv
2. Read both csv with pandas and create master dataframe with active cases per km calculation (new column)
3. Scrape NYC county numbers from: https://www.worldometers.info/coronavirus/usa/new-york/
4. For land area, use column L in the excel file and convert to km if need be.
5. Review NY Times implementation of mapbox covid maps



