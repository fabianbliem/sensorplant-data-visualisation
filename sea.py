import pandas as pd
import seaborn as sns
import warnings
import matplotlib.pyplot as plt

# We'll also import seaborn, a Python graphing library
warnings.filterwarnings("ignore")

sns.set(style="white", color_codes=True)

iris = pd.read_csv("./data.csv")  # the iris dataset is now a Pandas DataFrame
iris.head(10)  # View first 10 data rows