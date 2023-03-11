

# Load File
import pandas
import pandas as pd

data = pd.read_csv('mushroom.csv', header=None)
print(data.head(20))

print("Part Two")
# import pandas.api.types
# import pandas.api.types

for col in data.columns:
    if not pandas.api.types.is_numeric_dtype(data[col]):
        print(data[col].value_counts())

print(data.describe(include='all'))
