import pandas as pd

newdf=pd.read_excel(r"./Source Files/Processed FEDIAP INFOODS.xlsx")
gettheindexdf=pd.read_csv(r"./Source Files/NUTRIENT NAME.csv",encoding='latin-1')

print(gettheindexdf)