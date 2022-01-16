import pandas as pd
import numpy as np
df = pd.read_csv('crx.data', header=None)
df = df.replace('?', np.nan)

nb_obj = len(df.columns)
nb_attr = len(df)

nb_class = len(df[15][1:].unique())

print("Nb attribute : ", nb_obj)
print("Nb object : ", nb_attr)
print("Nb class : ", nb_class)
print(df.describe())
missing_values = df.isna().mean().round(4) * 100
print("Missing values per column : ", missing_values)

#Part 2 analysis
df = df.replace('00000', np.nan)
df = df.replace('a', 'male')
df = df.replace('b', 'female')
df = df.replace('f', False)
df = df.replace('t', True)
attributes = ["Gender","Age","debt","married","bankCustomer",
 "EducationLevel","Ethnicity","YearsEmployed","PriorDefault",
 "Employed","CreditScore","DriversLicense","Citizen","ZipCode","Income","class"]
df = df.set_axis(attributes, axis=1)
print(df)
#Drop column Zipcode
df = df.drop('ZipCode', axis = 1)
#Set column type to float
df["Age"] = df["Age"].astype("float64")
print(df["Age"])
hist = df.hist(column="Age")

df.hist( cumulative = True )

df.boxplot(by ='Age', column =['YearsEmployed'], grid = True)


pd.plotting.scatter_matrix(df[["Age", "debt", "YearsEmployed"]])

