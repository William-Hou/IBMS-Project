import csv
from matplotlib import pyplot as plt
import scipy.stats.stats

months =["January", "February", "March", "April", "May", "June",
         "July", "August", "September", "October", "November", "December"
         ]
years=[]

# Creates list of years from 1996 to 2016
for year in range(1996, 2016+1):
    years.append(str(year))

# Creates a list in the format [Month Year]
def create_dates(months = months, years = years):
    date_list = []
    month_counter = 0
    year_counter = 0
    for i in range(0,253):
        if year_counter < len(years):
            # Creates string in the format 'Month Year'
            date_string = years[year_counter] + " " + months[month_counter]
            # Adds each month to the list
            date_list.append(date_string)
            month_counter += 1
            # Re-cycles through months after each year
            if month_counter == 12:
                year_counter += 1 
                month_counter = 0
#    print date_list
    return date_list

#Generates list of x(gas) coordinates and y(cci) coordinates
def prepare_scatter(gas_data , cci_data): 
    gas_x = []
    cci_y = []
    counter = 0
    
    for row in gas_data:
        if counter != 0:
            #Add values to x(gas) list and converts them to floats
            gas_x.extend([float(i) for i in row[1:]])
        counter += 1
    counter = 0
    for row in cci_data:
        if counter != 0:
            #Add values to y(cci) list and converts them to floats
            cci_y.extend([float(i) for i in row[6:7]])
        counter += 1
    return (gas_x, cci_y)
    
# Plots gas price each month against CCI
def plot_data(gas_x, cci_y): 
    plt.xlabel("Gas Prices($)")
    plt.ylabel("Consumer Confidence Index")
    plt.title("Relationships between Gas Prices and the Consumer Confidence Index", weight='bold', y=1.02, fontsize=13)
    plt.text(3, 102, "r= ", fontsize = 14)
    plt.text(3.15, 102, r, fontsize = 14)
    plt.scatter(gas_x, cci_y)
    plt.show();

def get_pearsonr(gas_x, cci_y):
    r, p = scipy.stats.pearsonr(gas_x, cci_y)
    return r, p
    

with open("data/gas.csv",'r') as gascsv, open("data/cci.csv",'r') as ccicsv:
    readgas = csv.reader(gascsv)
    readcci = csv.reader(ccicsv)
    # Preares raw data into two lists: gas_x and cci_y
    gas_x, cci_y = prepare_scatter(readgas, readcci)
    # Calculates the Pearson Correlation Coefficient
    r, p = get_pearsonr(gas_x, cci_y)
    # Plot gas price against cci index
    plot_data(gas_x, cci_y)
    # Creates list of dares in form [Month Year]
    date_list = create_dates()


    
    
    
# Exports calculated data to csv file
"""
def write_to_csv(date_list, gas_x, cci_y):
    with open("finalcsv.csv", "w") as finalcsv:
        #Creates CSV Headers
        finalcsv.write("Date,")
        finalcsv.write("Gas Price,")
        finalcsv.write("CCI Index")
        finalcsv.write("\n")
        for x, y, z in zip(date_list, gas_x, cci_y):
            temp = str(x) + "," + str(y) + "," + str(z) + "\n"
            finalcsv.write(temp)
        print "completed!"

write_to_csv(date_list, gas_x, cci_y)
"""
