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
    def plot_data(gas_price, cci_value):
        plt.xlabel("Gas Prices($)")
        plt.ylabel("Consumer Confidence Index")
        plt.title("Relationships between Gas Prices and the Consumer Confidence Index", weight='bold', y=1.02,
                  fontsize=13)
        plt.text(3, 102, "r= ", fontsize=14)
        plt.text(3.15, 102, r, fontsize=14)
        plt.scatter(gas_price, cci_value)
        plt.show()


    def get_pearsonr(gas_price, cci_value):
        r, p = stats.pearsonr(gas_price, cci_value)
        return r, p


    # Prepares raw data into two lists: gas_x and cci_y
    gas_x, cci_y = prepare_scatter()

    if __name__ == "__main__":
        # Calculates the Pearson Correlation Coefficient
        r, p = get_pearsonr(gas_x, cci_y)
        # Plot gas price against cci index
        plot_data(gas_x, cci_y)


    def created_scatter():
        return gas_x, cci_y
