# This file exports the processed data into a csv file
from calculations import created_scatter

gas_x, cci_y = created_scatter()

months = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"
          ]
years = []

# Creates list of years from 1996 to 2016
for year in range(1996, 2016 + 1):
    years.append(str(year))


# Creates a list in the format [Month Year]
def create_dates(months=months, years=years):
    date_list = []
    month_counter = 0
    year_counter = 0
    for i in range(0, 253):
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


def write_to_csv(date_list, gas_x, cci_y):
    with open("data/finalcsv.csv", "w") as finalcsv:
        # Creates CSV Headers
        finalcsv.write("Date,")
        finalcsv.write("Gas Price,")
        finalcsv.write("CCI Index")
        finalcsv.write("\n")
        for x, y, z in zip(date_list, gas_x, cci_y):
            temp = str(x) + "," + str(y) + "," + str(z) + "\n"
            finalcsv.write(temp)
        print("completed!")


write_to_csv(create_dates(), gas_x, cci_y)
