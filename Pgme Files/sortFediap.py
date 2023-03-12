import pandas as pd

newdf=pd.read_excel(r"./Source Files/Processed FEDIAP INFOODS.xlsx")
newdf["Nut ID"]=(newdf["Nut ID"].fillna(0).astype("int")).astype("str")

gettheindexdf=pd.read_csv(r"./Source Files/NUTRIENT NAME.csv",encoding='latin-1')
print(gettheindexdf)

newdict=dict(zip(gettheindexdf["NutrientID"].astype("str"),gettheindexdf["Tagname"]))

newdf["InFoods"]=newdf["Nut ID"].replace(newdict,regex=True)
newdf.loc[newdf["Nut ID"]=="307","InFoods"]="NA"
newdf.loc[newdf["Nut ID"]=="302","InFoods"]="CL"
newdf.loc[newdf["Nut ID"]=="314","InFoods"]="I"
print(newdf["Nut ID"][20:30])
newdf.to_csv(r"./Source Files/limitsexpand.csv",encoding='latin-1')

