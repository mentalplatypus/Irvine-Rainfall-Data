import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# data taken from https://ceorange.ucanr.edu/about/weather/?weather=station&station=75
# remove first row of dataframe
data = pd.read_csv("data.csv")
data.drop(index=data.index[0],
          axis=0,
          inplace=True)
# (list(data.columns))

# data['Unnamed: 0'] = data['Unnamed: 0'].astype(float)
data['2022.1'] = data['2022.1'].astype(float)
data['2021.1'] = data['2021.1'].astype(float)
data['2020.1'] = data['2020.1'].astype(float)
data['2019.1'] = data['2019.1'].astype(float)

data.rename({"Unnamed: 0": "Month", "2022.1": "2022 Total Rainfall", "2021.1": "2021 Total Rainfall",
             "2020.1": "2020 Total Rainfall", "2019.1": "2019 Total Rainfall"}, axis=1, inplace=True)

# Plot a simple line chart
# fig, ax = plt.subplots()
# lines = ax.plot(data)
# ax.set_title("Click somewhere on a line.\nRight-click to deselect.\n"
# "Annotations can be dragged.")

plt.plot(data['Month'], data['2019 Total Rainfall'], marker='.', label='2019')

# Plot another line on the same chart/graph
plt.plot(data['Month'], data['2020 Total Rainfall'], marker='.', label='2020')
plt.plot(data['Month'], data['2021 Total Rainfall'], marker='.', label='2021')
plt.plot(data['Month'], data['2022 Total Rainfall'], marker='.', label='2022')

plt.title("Irvine Total Rainfall from 2019 to 2022 by Month")
plt.xlabel("Month")
plt.ylabel("Total Rainfall (in inches)")
plt.legend()
plt.margins(x=0)
plt.grid(True, linestyle='dashed', axis='y')

plt.show()
