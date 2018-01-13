import csv
from matplotlib import pyplot as plt
from scipy import stats

with open("data/gas.csv", 'r') as gascsv, open("data/cci.csv", 'r') as ccicsv:
    readgas = csv.reader(gascsv)
    readcci = csv.reader(ccicsv)


    # Generates list of x(gas) coordinates and y(cci) coordinates
    def prepare_scatter(gas_data=readgas, cci_data=readcci):
        gas_x = []
        cci_y = []
        counter = 0

        for row in gas_data:
            if counter != 0:
                # Add values to x(gas) list and converts them to floats
                gas_x.extend([float(i) for i in row[1:]])
            counter += 1
        counter = 0
        for row in cci_data:
            if counter != 0:
                # Add values to y(cci) list and converts them to floats
                cci_y.extend([float(i) for i in row[6:7]])
            counter += 1
        return (gas_x, cci_y)


    # Plots gas price each month against CCI
    def plot_data(gas_price, cci_value, y1, y2):
        plt.xlabel("Gas Prices($)")
        plt.ylabel("Consumer Confidence Index")
        plt.title("Relationships between Gas Prices and the Consumer Confidence Index", weight='bold', y=1.02,
                  fontsize=13)
        plt.text(3, 102, "r=", fontsize=14)
        plt.text(3.25, 102, r, fontsize=14)
        plt.scatter(gas_price, cci_value, color='k', alpha=.90)
        plt.plot([0, 4.50], [y1, y2], color='r', lw=2)
        plt.xlim(0,5)
        plt.ylim(y2)
        plt.show()


    def get_pearsonr(gas_price, cci_value):
        slope, intercept, r_value, p_value, std_err = stats.linregress(gas_price, cci_value)
        y1 = intercept
        y2 = float(slope) * (4.50) + float(intercept)
        return r_value, p_value, y1, y2


    # Prepares raw data into two lists: gas_x and cci_y
    gas_x, cci_y = prepare_scatter()

    # This code won't run when imported
    if __name__ == "__main__":
        # Calculates the Pearson Correlation Coefficient
        r, p, y1, y2 = get_pearsonr(gas_x, cci_y)
        # Plot gas price against cci index
        plot_data(gas_x, cci_y, y1, y2)


    def created_scatter():
        return gas_x, cci_y
