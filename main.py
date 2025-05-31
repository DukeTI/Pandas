## Import all modules
import pandas as pd
import numpy as np

"""Create basic dataframe (a table for data values)"""
df = pd.DataFrame(
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],  # Raw values
    columns=["a", "b", "c"],  # Headers to dataframe
    index=["x", "y", "z"],  # Indices (rows - headers) for dataframe
)


"""Load in pre-existing dataframes"""
coffee = pd.read_csv("warmup-data/coffee.csv")
df.head()

# Parquet is same as csv but takes up less storage
results = pd.read_parquet("./data/results.parquet")


"""Basic functions"""
results.head(10)  # Print the first 10 rows of the dataframe
results.shape  # Print the shape of the dataframe (rows, columns)

# print(coffee)  # Prints the entire dataframe - !! Don't use on large dataframes

coffee.sample(5)  # Returns a random sample of data - just to get a feel of things


"""To return specific data"""
coffee.loc[
    0:3, "Day"
]  # .loc to specify exact data to be returned - defined by row and column (in that order)
## NB to specify multiple, put into a list: """coffee.loc[[2,3,5], ["Day", "Units Sold"]]"""
coffee.iloc[:, [0, 2]]  # To specify columns - integer based


"""To return specific values"""
coffee.at[0, "Day"]  # Can only be ONE value, so not 1:3
coffee.iat[0, 0]  # For integer based sorting


"""Editing indices - can be easier to sort"""
coffee.index = coffee["Day"]  # So to sort from monday through wednesday .. ->
coffee.loc["Monday":"Wednesday", "Units Sold"]


"""Editing data in dataframe"""
coffee.loc[1, "Units Sold"] = 25
# coffee.loc[1:3, "Units Sold"] = 25  # To modify multiple values


"""Sorting dataframe"""
coffee.sort_values(
    "Units Sold", ascending=True
)  # Sorts data by values in specified column


"""Filtering data"""
bios = pd.read_csv("data/bios_new.csv")
newdataset = bios.loc[bios["height_cm"] > 215, ["name", "height_cm"]]
# OR shorthand = ..
newdataset = bios[bios["height_cm"] > 215][["name", "height_cm"]]
newdataset = newdataset.sort_values("height_cm", ascending=False)
# print(newdataset)

##For multiple filters
newdataset = bios[(bios["height_cm"] > 215) & (bios["born_country"] == "USA")]
# print(newdataset[["name", "height_cm", "born_country"]])

## Can also specify conditions that are fulfilled by two possible conditions
newdataset = bios[bios["name"].str.contains("bob|david", case=False)]
newdataset = bios[bios["born_country"].isin(["GBR", "RUS", "USA"])]
# print(newdataset[["name", "born_country"]])

# Can also be used with query
newdataset = bios.query("born_country == 'GBR' & name.str.startswith('Bob')")
# print(newdataset[["name", "born_country"]])


"""Adding columns"""
coffee["price"] = 3.50
# print(coffee.head())

# Adding columns with values specific to certain condition within the data frame
coffee["new_price"] = np.where(coffee["Coffee Type"] == "Espresso", 3, 4.99)
# print(coffee.sample(5))

"""Removing / Dropping columns"""
coffee.drop(
    columns=["price"], inplace=True
)  # inplace means that it actually edits the dataframe; without it it won't modify it, just print a modified version
# or .. coffee = coffee.drop(columns=["price"])
# or .. coffee = coffee[["Day", "Coffee Type", "Units Sold"]] # Just keep the ones you need
# print(coffee.sample(5))

"""Creating columns in relation to pre-existing columns"""
coffee["revenue"] = coffee["new_price"] * coffee["Units Sold"]
# print(coffee.sample(5))
bios_new = bios.copy()
bios_new["first_name"] = bios_new["name"].str.split(" ").str[0]
print(bios_new[["first_name"]])

"""Renaming columns"""
coffee.rename(columns={"new_price": "Price"}, inplace=True)
# print(coffee.head())
