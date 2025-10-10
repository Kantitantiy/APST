import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import MoreGraphs as mg

def basedata():
    # Fixed seed for randomness
    np.random.seed(42)
    # Data for 36 months
    months = pd.date_range(start='2020-01', periods=36, freq='ME')
    # Seasonality + noise
    demand = 100 + 10*np.sin(2*np.pi*months.month/12) + np.random.normal(0, 5, 36)
    # Creating a DataFrame
    data = pd.DataFrame({'Month': months, 'Demand': demand})
    print(data.head())
    return data

def autocorrelation(series, lag):
    return series.autocorr(lag=lag)

def prepare_lags(data, lag):
    # Lag values between 0-12
    lags = list(range(0, lag+1))
    acf_values = [autocorrelation(data['Demand'], lag) for lag in lags]
    acf_df = pd.DataFrame({'Lag': lags, 'ACF': acf_values})
    print(acf_df)
    return acf_df

def plot_autocorrelation(acf_df):
    plt.figure(figsize=(8,5))
    sns.barplot(x='Lag', y='ACF', data=acf_df, color='skyblue', edgecolor='black')
    plt.axhline(0, color='black', linewidth=1)
    plt.title('Autocorrelation Function (ACF)', fontsize=14)
    plt.xlabel('Lag')
    plt.ylabel('Autocorrelation')
    plt.show()

def plot_data(data):
    # assuming `data` has columns: Month, Demand
    lags = list(range(0, 37))  # 0..36
    acf_values = [data['Demand'].autocorr(lag=l) for l in lags]
    acf_df = pd.DataFrame({'Lag': lags, 'ACF': acf_values})

    fig, ax = plt.subplots(figsize=(10,4))
    ax.plot(data['Month'], data['Demand'], marker='o')
    ax.set_title('Monthly Demand (36 Months)', fontsize=13)
    ax.set_xlabel('Month'); ax.set_ylabel('Demand')
    fig.autofmt_xdate()

    # Draw a dashed vertical line at the start of each year (except the first year)
    years = sorted(data['Month'].dt.year.unique())
    for y in years[1:]:
        ax.axvline(pd.Timestamp(y, 1, 1), linestyle='--', linewidth=1, color='gray')

    # Add year labels at the top of the chart
    ymax = ax.get_ylim()[1]  # Get the top limit of the y-axis
    for y in years:
        ax.text(pd.Timestamp(y, 7, 1), ymax, str(y),
                ha='center', va='bottom', fontsize=9)

    plt.show()

data=basedata()
acf_df = prepare_lags(data, 12)
plot_autocorrelation(acf_df)
plot_data(data)
