import pandas as pd

series1 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
series2 = pd.Series([2.2, None, 3.0, 1.5], index=['a', 'b', 'c', 'd'])
series3 = pd.Series(['q', 'q', 'z', 'z'], index=['a', 'b', 'c', 'd'])

df = pd.DataFrame({'s1': series1, 's2': series2, 's3': series3})

print(df)

print(df.iloc[:2, :2])
print(df.loc [:'b', ['s1', 's2', 's3']])