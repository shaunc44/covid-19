"""
Calculate activate case per sq km of US counties
"""

import pandas as pd
# pd.set_option('display.precision', 10)



def get_land_df(path, km_sq_to_mi):
    df = pd.read_csv(path, usecols=['Areaname', 'LND110210D'])
    df['km_sq'] = df.LND110210D * km_sq_to_mi
    df.rename(columns={'LND110210D': 'mi_sq'}, inplace=True)
    # round to two decimal places in python pandas 
    pd.options.display.float_format = '{:.2f}'.format
    return df


def get_cases_df(path):
    df = pd.read_csv(path)


if __name__ == '__main__':
    land_path = '../data/us_land_area/us_county_land_area.csv'
    cases_path = '../data/us_daily/2020-08-22.csv'
    km_sq_to_mi = 2.589975

    df = get_land_df(land_path, km_sq_to_mi)

    df2 = get_cases_df(cases_path)

    # import pdb
    # pdb.set_trace()















