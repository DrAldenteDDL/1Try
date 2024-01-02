# main.py
from alpha_vantage_data import AlphaVantageData
from data_plotter import DataPlotter
from company_overview import CompanyOverview

def main():
    api_keys = ['000P45DRHLJACJR5','NJSCKDJ4CQUGS3W2','TOT0MLJY16O2BLA9']
    alpha_vantage_data = AlphaVantageData(api_keys)
    data_plotter = DataPlotter()
    company_overview = CompanyOverview(api_keys)

    symbol = input("Enter the stock ticker symbol: ").upper()
    count_of_years_input = input("Enter the count of years to display: ")

    try:
        count_of_years = int(count_of_years_input)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        count_of_years = None

    earnings_data = alpha_vantage_data.get_earnings_data(symbol)
    print(earnings_data)
    #data_plotter.plot_earnings_data(earnings_data, symbol, count_of_years)

    #income_data = alpha_vantage_data.get_income_statement_data(symbol)
    #data_plotter.plot_income_statement(income_data, symbol)
    
    #alpha_vantage_data.get_balance_sheet_data(symbol)
    
    #alpha_vantage_data.get_cash_flow_data(symbol)

    #overview_data = company_overview.get_overview_data(symbol)
    #company_overview.show_overview(overview_data, symbol)

if __name__ == "__main__":
    main()
