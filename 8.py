#8. Analyze a dataset containing information about the sales revenue and advertising expenditure of a company over a period of time.
#Calculate the Karl Pearson correlation coefficient between sales revenue and advertising expenditure using Python. 
#Interpret the correlation coefficient and discuss the strength and direction of the relationship between advertising and sales.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

data = pd.read_csv("sales_dataset.csv")  # Replace "sales_dataset.csv" with the actual file name

sales_revenue = data['Sales _revenue(thousands)']
advertising_expenditure = data['Advertising_exp(millions)']

correlation_coefficient, p_value = pearsonr(sales_revenue, advertising_expenditure)

if correlation_coefficient > 0:
    correlation_direction = "positive"
elif correlation_coefficient < 0:
    correlation_direction = "negative"
else:
    correlation_direction = "no"

correlation_strength = abs(correlation_coefficient)

print("Correlation Coefficient:", correlation_coefficient)
print("Correlation Direction:", correlation_direction)
print("Correlation Strength:", correlation_strength)

plt.scatter(advertising_expenditure, sales_revenue)
plt.xlabel("Advertising Expenditure")
plt.ylabel("Sales Revenue")
plt.title("Relationship between Advertising Expenditure and Sales Revenue")
plt.show()
