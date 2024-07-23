#5. You are given a dataset containing the prices of houses in a neighborhood. 
#Perform univariate analysis on this dataset using Python and calculate the mean, median, mode, and standard deviation of the house prices. 
#Additionally, plot a box plot to visualize the distribution of prices. Write a Python program to implement this analysis.
#house_prices = [300000, 350000, 320000, 280000, 400000, 380000, 330000, 310000, 290000, 270000, 350000, 380000, 370000]
import numpy as np
import matplotlib.pyplot as plt

house_prices = [300000, 350000, 320000, 280000, 400000, 380000, 330000, 310000, 290000, 270000, 350000, 380000, 370000]

mean_price = np.mean(house_prices)
print("Mean price:", mean_price)

median_price = np.median(house_prices)
print("Median price:", median_price)

mode_price = np.argmax(np.bincount(house_prices))
print("Mode price:", mode_price)

std_price = np.std(house_prices)
print("Standard deviation:", std_price)

plt.boxplot(house_prices)
plt.ylabel("Price")
plt.title("Distribution of House Prices")
plt.show()
