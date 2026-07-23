#
# @(#)dates_2024.py 2024.1
#
# Copyright (c) 2024 by DPAEVD
# All rights reserved
#
# author: Daniele Denti (daniele.denti@bluewin.ch)
#

import argparse
import pandas as pd
from datetime import datetime, timedelta

def create_excel_with_dates(year):
    start_date = datetime(year, 1, 1)
    end_date = datetime(year, 12, 31)
    delta = end_date - start_date

    dates = [(start_date + timedelta(days=i)).strftime('%d.%m.%Y') for i in range(delta.days + 1)]
    df = pd.DataFrame(dates, columns=['Date'])
    df.to_excel(f'dates_{year}.xlsx', index=False)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate an Excel file with all dates for a given year.')
    parser.add_argument('--year', type=int, default=datetime.now().year,
                        help='The year to generate dates for (default: current year)')
    args = parser.parse_args()
    
    create_excel_with_dates(args.year)
    exit(0)
