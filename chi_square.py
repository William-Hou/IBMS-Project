from calculations import created_scatter
from scipy import stats

gas_x, cci_y = created_scatter()


def create_contingency(gas_x=gas_x, cci_y=cci_y):
    quartiles = [0, 25, 50, 75, 100]
    quartile_values = []
    for i in range(0, 5):
        quartile_values.append(stats.scoreatpercentile(gas_x, quartiles[i]))
    print quartile_values


create_contingency()
