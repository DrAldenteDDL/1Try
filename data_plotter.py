# data_plotter.py
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd

class DataPlotter:
    def plot_earnings_data(self, earnings_df, symbol, count_of_years=None):
        if earnings_df is not None and not earnings_df.empty:
            # Filter the DataFrame to show only the specified count of years from the youngest data point
            if count_of_years is not None:
                earnings_df = earnings_df.nlargest(count_of_years, 'year')

            # Calculate percentage change relative to the year before
            earnings_df['percentage_change'] = (earnings_df['reportedEPS'].shift(1) - earnings_df['reportedEPS']) / earnings_df['reportedEPS'] * 100

            # Plotting the data
            plt.figure(figsize=(10, 6))
            ax = plt.subplot(111)

            # Bar plot for earnings
            bars = ax.bar(earnings_df['year'], earnings_df['reportedEPS'], color='blue', label='Earnings')

            # Display percentage change as text on each bar
            for i, (bar, pct) in enumerate(zip(bars, earnings_df['percentage_change'])):
                height = bar.get_height()
                if i > 0:  # Skip the first bar as there is no prior year for percentage change
                    ax.text(bar.get_x() + bar.get_width() / 2, height, f'{pct:.2f}%', ha='center', va='bottom', color='black')

            ax.set_xlabel('Year')
            ax.set_ylabel('Earnings Per Share (EPS)', color='blue')

            ax.grid(True)
            plt.title(f'{symbol} Annual Earnings Per Share with Percentage Change to Prior Year')
            plt.show()
        else:
            print("No data to plot.")

    def plot_income_statement(self, income_data, symbol):
        if income_data is not None:
            ax = income_data.plot(kind='bar', figsize=(10, 6))
            ax.set_title(f'Income Statement for {symbol}')
            ax.set_xlabel('Fiscal Year')
            ax.set_ylabel('Amount (in billions)')
            ax.set_xticklabels(income_data.index, rotation=45, ha='right')
            ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f'{x / 1e9:.1f}B'))
            plt.show()
        else:
            print("No income statement data to plot.")