import pandas as pd
from traits.trait_types import false

#DataFrames
series = pd.Series(["Marruti", "Mahindra", "KIA"])
colors = pd.Series(["Blue", "White", "Red"])
car_data = pd.DataFrame({"car_make":series, "colors":colors})

#import/export data
test_import= pd.read_csv("heart-disease.csv")
# test_import.to_excel("test.xlsx", index=False)

#mean of the data
car_sales=pd.read_csv("car-sales.csv")
print(car_sales.mean(numeric_only=True))
print(car_sales.dtypes )
print(car_sales.describe())
print(car_sales["Doors"].sum())

print(car_sales.loc[2])
print(car_sales.iloc[2])