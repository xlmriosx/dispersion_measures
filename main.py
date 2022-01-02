import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plot

df = pd.read_csv('cars.csv')

print(df['price_usd'].std())

rango = df['price_usd'].max() - df['price_usd'].min()
print(rango)

median = df['price_usd'].median()
Q1 = df['price_usd'].quantile(q=0.25)
Q3 = df['price_usd'].quantile(q=0.75)
min_val = df['price_usd'].quantile(q=0)
max_val = df['price_usd'].quantile(q=1.0)
print(min_val, Q1, median, Q3, max_val)

iqr = Q3 - Q1
print(iqr)

minlimit = Q1 - 1.5*iqr
maxlimit = Q3 + 1.5*iqr
print('rango para detección de outliers: {}, {}'.format(minlimit, maxlimit))

sns.set(rc={'figure.figsize':(11.7, 8.27)})
f, (ax_hist, ax_box) = plot.subplots(2, sharex=True, gridspec_kw={"height_ratios": (.6, .4)})
sns.histplot(df['price_usd'], ax=ax_hist)
sns.boxplot(df['price_usd'], ax=ax_box)
ax_hist.set(xlabel='')
plot.show()

sns.boxplot(x = 'engine_fuel', y = 'price_usd', data = df)
plot.show()