import pandas as pd
import matplotlib.pyplot as plt


def main():
    """Load the bike buyers dataset, compute summary statistics and plot buyers/non-buyers by region."""
    # Load the Excel file (expects it to be in the same directory)
    file_name = 'Excel Project Dataset.xlsx'
    # Read the main worksheet
    df = pd.read_excel(file_name, sheet_name='bike_buyers')

    # Compute counts of buyers vs non-buyers by region
    summary = df.groupby(['Region', 'Purchased Bike']).size().unstack(fill_value=0)
    print('Counts by region and purchase decision:')
    print(summary)

    # Create a bar chart
    ax = summary.plot(kind='bar')
    ax.set_title('Bike Purchase Decisions by Region')
    ax.set_xlabel('Region')
    ax.set_ylabel('Number of People')
    # Move the legend outside the plot for readability
    ax.legend(title='Purchased Bike', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.savefig('purchased_by_region.png')
    plt.close()


if __name__ == '__main__':
    main()
