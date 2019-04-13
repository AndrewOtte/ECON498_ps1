import numpy as np
import pandas as pd
import statsmodels.formula.api as smf
import statsmodels.api as sm
from sklearn import linear_model

df = pd.read_csv("parsed_results/cmc_dataset.csv")

X = df[['Price' , 'Circulating_Supply' , 'Volume']]
Y = df[['Market_Cap']]

x = sm.add_constant(X)
result= sm.OLS(Y,X).fit()

print(result.summary())



target = df.iloc[:,2]
data = df.iloc[:,2:6]

regression = linear_model.LinearRegression()

regression.fit(data, target)

X = [
	[90588631815.3,5137.5544007,17632637.0,17051926081.3],
	[17610809398.0,166.83023295,105561258.812,7358728043.72],
	[14921626515.0,0.357457610487,41743765071.0,1489814713.69],
]

results = regression.predict(X)
print("Market Cap Predictions for BTC, ETH and XRP")
print(results)