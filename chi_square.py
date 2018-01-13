from calculations import created_scatter
from scipy import stats
import statistics
import numpy as np

gas_x, cci_y = created_scatter()

print(statistics.mean(gas_x))
print(statistics.mean(cci_y))


def create_contingency_table(gas_price=gas_x, cci_value=cci_y):
    gas_mean = statistics.mean(gas_x)
    cci_mean = statistics.mean(cci_y)
    # First 2 values are gas prices, last 2 values are cci values
    observed_values = []

    # Sorts all gas prices according to their position above/below the mean
    observed_values.append(len(list(filter(lambda x: x < gas_mean, gas_price))))
    observed_values.append(len(list(filter(lambda x: x >= gas_mean, gas_price))))
    # Sorts all cci values according to their position above/below the mean
    observed_values.append(len(list(filter(lambda x: x < cci_mean, cci_value))))
    observed_values.append(len(list(filter(lambda x: x >= cci_mean, cci_value))))

    print(observed_values)
    observed_values = np.array(observed_values).reshape(2, 2)
    print(observed_values)
    chi2, p, _, _ = stats.chi2_contingency(observed_values, True)
    print("The Chi Square value is", chi2, '\n', "The p value is", p)


create_contingency_table()
