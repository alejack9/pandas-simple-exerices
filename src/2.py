import pandas as pd
df = __import__('1').df

df['Spettacolo_OK'] = df.loc[:, 'Numero Goal'].map(lambda x: x > 150)


def exec():
    print(df)


if __name__ == '__main__':
    exec()
