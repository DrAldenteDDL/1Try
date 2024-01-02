# company_overview.py
import pandas as pd
from alpha_vantage.fundamentaldata import FundamentalData

class CompanyOverview:
    def __init__(self, api_key):
        self.api_key = api_key

    def get_overview_data(self, symbol):
        fd = FundamentalData(key=self.api_key, output_format='pandas')
        overview_data, meta_data = fd.get_company_overview(symbol=symbol)

        if 'Error Message' in meta_data:
            print(f"Error: {meta_data['Error Message']}")
            return None

        return overview_data

    def show_overview(self, overview_data, symbol):
        if overview_data is not None and isinstance(overview_data, pd.DataFrame):
            print(f"Available columns in overview_data for {symbol}:")
            print(overview_data.columns)
        elif overview_data is None:
            print(f"No overview data available for the specified symbol: {symbol}.")
        else:
            print(f"Unexpected type for overview_data. Expected DataFrame, got {type(overview_data)}.")