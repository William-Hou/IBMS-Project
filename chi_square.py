from calculations import created_scatter
from scipy import stats

gas_x, cci_y = created_scatter()


def create_contingency(gas_price=gas_x, cci_value=cci_y):
    quartiles = [0, 25, 50, 75, 100]
    quartile_values = []
    for i in range(0, 5):
        quartile_values.append(stats.scoreatpercentile(gas_price, quartiles[i]))
    print(quartile_values)


create_contingency()
