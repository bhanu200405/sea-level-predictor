import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Import data
df = pd.read_csv("epa-sea-level.csv")

def draw_plot():
    # Create scatter plot
    fig, ax = plt.subplots(figsize=(12,6))
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', label='Data')

    # Line of best fit (all years)
    res_all = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_all = pd.Series(range(df['Year'].min(), 2051))
    line_all = res_all.intercept + res_all.slope * years_all
    ax.plot(years_all, line_all, 'r', label='Best Fit (All Years)')

    # Line of best fit (year >= 2000)
    df_2000 = df[df['Year'] >= 2000]
    res_2000 = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    years_2000 = pd.Series(range(2000, 2051))
    line_2000 = res_2000.intercept + res_2000.slope * years_2000
    ax.plot(years_2000, line_2000, 'green', label='Best Fit (2000+)')

    # Labels, title, legend
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")
    ax.legend()

    # Save and show figure
    fig.savefig("sea_level_plot.png")
    plt.show()
    return fig

if __name__ == "__main__":
    draw_plot()
    print("Plot saved as sea_level_plot.png")
