# alpha_vantage_data.py
import pandas as pd
import requests

class AlphaVantageData:
    def __init__(self, api_keys):
        self.api_keys = api_keys
        self.current_api_key_index = 0
        self.requests_counter = 0

    def _api_request(self, function, symbol):
        # Use the current API key
        api_key = self.api_keys[self.current_api_key_index]
        url = f'https://www.alphavantage.co/query?function={function}&symbol={symbol}&apikey={api_key}'
        r = requests.get(url)
        data = r.json()
        self.requests_counter += 1

        # Switch to the next API key after 25 requests
        if self.requests_counter >= 25:
            self.current_api_key_index = (self.current_api_key_index + 1) % len(self.api_keys)
            self.requests_counter = 0

        return pd.DataFrame(data.get('annualEarnings', [])), data.get('metaData', {})

    def get_earnings_data(self, symbol):
        earnings_df, meta_data = self._api_request('EARNINGS', symbol)
        
        if 'Error Message' in meta_data:
            print(f"Error: {meta_data['Error Message']}")
            return None
        
        # Print column names for inspection
        print("Column names in earnings_df:")
        print(earnings_df.columns)
        
        if not earnings_df.empty:
            earnings_df = earnings_df.drop(0, axis=0)

        earnings_df['reportedEPS'] = pd.to_numeric(earnings_df['reportedEPS'], errors='coerce')
        earnings_df['year'] = pd.to_datetime(earnings_df['fiscalDateEnding']).dt.year
        return earnings_df

    def get_income_statement_data(self, symbol):
        income_data, meta_data = self._api_request('INCOME_STATEMENT', symbol)
        columns_to_plot = ['totalRevenue', 'netIncome']
        income_data[columns_to_plot] = income_data[columns_to_plot].apply(pd.to_numeric, errors='coerce')
        income_data['Year'] = pd.to_datetime(income_data['fiscalDateEnding']).dt.year
        income_data.set_index('Year', inplace=True)
        income_data = income_data[::-1]
        return income_data

    def get_balance_sheet_data(self, symbol):
        balance_sheet_data, meta_data = self._api_request('BALANCE_SHEET', symbol)
        print(balance_sheet_data)
        #columns_to_plot = ['totalRevenue', 'netIncome']
        #balance_sheet_data[columns_to_plot] = balance_sheet_data[columns_to_plot].apply(pd.to_numeric, errors='coerce')
        #balance_sheet_data['Year'] = pd.to_datetime(balance_sheet_data['fiscalDateEnding']).dt.year
        #balance_sheet_data.set_index('Year', inplace=True)
        #balance_sheet_data = balance_sheet_data[::-1]
        #return balance_sheet_data

    def get_cash_flow_data(self, symbol):
        cash_flow_data, meta_data = self._api_request('CASH_FLOW', symbol)
        print(cash_flow_data)
        #columns_to_plot = ['totalRevenue', 'netIncome']
        #cash_flow_data[columns_to_plot] = cash_flow_data[columns_to_plot].apply(pd.to_numeric, errors='coerce')
        #cash_flow_data['Year'] = pd.to_datetime(cash_flow_data['fiscalDateEnding']).dt.year
        #cash_flow_data.set_index('Year', inplace=True)
        #cash_flow_data = cash_flow_data[::-1]
        #return cash_flow_data