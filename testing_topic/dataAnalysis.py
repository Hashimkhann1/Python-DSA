import pandas as pd
import matplotlib.pyplot as plt

# Load data from a CSV file
data = pd.read_csv("sales_data.csv")

# Explore the data
print(data.head())
print(data.describe())

# Visualize the data
plt.scatter(data['sales'], data['profit'])
plt.xlabel('Sales')
plt.ylabel('Profit')
plt.title('Sales vs. Profit')
plt.show()