import pandas as pd
df1 = __import__('7').df1
df2 = __import__('7').df2
dfConcat = __import__('7').dfConcat

res = dfConcat.groupby('Tipologia')[
    'Pubblico'].apply(lambda x: x.max() - x.min())

print(res)
