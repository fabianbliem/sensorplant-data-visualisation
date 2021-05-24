# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# First, we'll import pandas, a data processing and CSV file I/O library

import pandas as pd
import plotly.express as px

df = pd.read_csv("./data-new-1mio-column.csv")

smooth_data = df.rolling(500).mean()
# smooth_data = df

fig = px.line(smooth_data, x='#', y='PlantData', title='Test')
fig.show()
# def print_hi(name):
# Use a breakpoint in the code line below to debug your script.
# print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
# print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
