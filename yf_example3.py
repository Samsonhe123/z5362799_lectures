"""Name of module: yf_example3.py
Download stock price data for Qantas for a given year and save the information in a CSV file."""

import os
import toolkit_config as cfg
import yf_example2

"""Taking in parameter, year, and then downloading the stock for that given year"""


def qan_prc_to_csv(year):
    tic = 'QAN.AX'
    name_of_file = f'qan_prc_{year}.cs'
    pth = os.path.join(cfg.DATADIR, name_of_file)
    yf_example2.yf_prc_to_csv(tic, pth, f'{year}-01-01', f'{year}-12-31')


if __name__ == "__main__":
    year = 2020
    qan_prc_to_csv(year)
