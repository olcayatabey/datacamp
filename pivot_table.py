
import pandas as pd
import seborn as sns

titanix=sns.load_dataset("titanic")
titanic.head()

titanic.groupby("sex")["survived"].mean()
titanic.groupby("sex")[["survived"]].mean()

titanic.groupby(["sex", "class"])[["survived"]].aggregate("mean")
titanic.groupby(["sex", "class"])[["survived"]].aggregate("mean").unstack() // easy to read

#pivot ile pivot_table

titanic.pivot_table("survıved", index="sex", columns="class")
titanic.age.head()

age= pd.cut(titanic["age"],[0,18,90})
age.head(10)
                            
titanic.pvot_table("survived",  ["sex",age],"class")                          

