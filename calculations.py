import csv
from matplotlib import pyplot as plt
from scipy import stats


# Generates list of x(gas) coordinates and y(cci) coordinates
def create_scatter(gas_data, cci_data):
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
def plot_data(gas_x, cci_y):
    plt.xlabel("Gas Prices($)")
    plt.ylabel("Consumer Confidence Index")
    plt.title("Relationships between Gas Prices and the Consumer Confidence Index", weight='bold', y=1.02,
              fontsize=13)
    plt.text(3, 102, "r= ", fontsize=14)
    plt.text(3.15, 102, r, fontsize=14)
    plt.scatter(gas_x, cci_y)
    plt.show();


def get_pearsonr(gas_x, cci_y):
    r, p = stats.pearsonr(gas_x, cci_y)
    return r, p


with open("data/gas.csv", 'r') as gascsv, open("data/cci.csv", 'r') as ccicsv:
    readgas = csv.reader(gascsv)
    readcci = csv.reader(ccicsv)
    # Prepares raw data into two lists: gas_x and cci_y
    gas_x, cci_y = create_scatter(readgas, readcci)
    # Calculates the Pearson Correlation Coefficient
    r, p = get_pearsonr(gas_x, cci_y)
    # Plot gas price against cci index
    plot_data(gas_x, cci_y)


def created_scatter():
    return gas_x, cci_y
