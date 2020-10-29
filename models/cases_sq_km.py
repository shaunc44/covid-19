"""
Calculate activate case per sq km of US counties
"""

import pandas as pd
import requests



def get_land_df(path, km_sq_to_mi):
    df = pd.read_csv(path, usecols=['Areaname', 'LND110210D'])
    df['km_sq'] = df.LND110210D * km_sq_to_mi
    df.rename(columns={'LND110210D': 'mi_sq'}, inplace=True)
    # round to two decimal places in python pandas 
    pd.options.display.float_format = '{:.2f}'.format
    return df


def get_nyc_cases():
    url = 'https://www.worldometers.info/coronavirus/usa/new-york/'
    header = {'User-agent': 'Mozilla/5.0'}
    req = requests.get(url, headers=header)
    df = pd.read_html(req.text)[1]

    nyc_counties = ['Bronx', 'Kings', 'Manhattan', 'Queens', 'Richmond']
    df_list = []
    for county in nyc_counties:
        df_list.append(df.loc[df['County'] == county])

    return pd.concat(df_list)


def get_cases_df(path):
    nyc_df = get_nyc_cases()
    df = pd.read_csv(path)
    # Need to insert ny counties into df

    import pdb
    pdb.set_trace()


if __name__ == '__main__':
    land_path = '../data/us_land_area/us_county_land_area.csv'
    cases_path = '../data/us_daily/2020-10-27.csv'
    km_sq_to_mi = 2.589975

    df = get_land_df(land_path, km_sq_to_mi)

    df2 = get_cases_df(cases_path)

    import pdb
    pdb.set_trace()















