import pandas as pd

df = pd.read_excel('pasdat.xlsx')

df['date'] = pd.to_datetime(df['date'], dayfirst=True)

df['date'] = df['date'].dt.strftime('%d%m%Y')

df.to_excel('transformed_pasdat.xlsx', index=False)
print('Transformation complete')
