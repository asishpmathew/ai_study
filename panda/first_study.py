import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("heart-disease.csv")
data.target.value_counts().plot(kind="bar")
plt.show()