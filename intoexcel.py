# importing the dependencies
import modin.pandas as pd

#%%
# importign the csv to pandas data frame and removing the unnamed colum
df = pd.read_csv("assaign03.csv")
df.drop("Unnamed: 0", axis=1, inplace=True)

#%%




