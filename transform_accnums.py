import pandas as pd

df = pd.read_excel("acc.xlsx")


def transform_account_number(account):
    parts = account.split('-')
    if len(parts) >= 3:
        first_three_part = parts[0]
        modified_middle = '0' + parts[1] + '0'

        if parts[-1] == '1590':
            last_part = '1005900'
        elif parts[-1] == '1591':
            last_part = '1005901'
        elif parts[-1] == '1650':
            last_part = '1006500'
        elif parts[-1] == '1730':
            last_part = '1007300'
        elif parts[-1] == '1600':
            last_part = '1006000'
        elif parts[-1] == '110':
            last_part = '1000100'
        else:
            last_part = parts[-1]
        return first_three_part + modified_middle + last_part
    else:
        return account


df['account number'] = df['account number'].astype(str).apply(transform_account_number)

df.to_excel('transformed_acc.xlsx', index=False)
print('Transformation complete')
