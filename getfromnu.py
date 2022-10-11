import pandas as pd
import glob
import os

path = r'C:/Python/myfinance/extratos_nubank/'
all_files = glob.glob(os.path.join(path , "*.csv"))

list_nu = []

for filename in all_files:
    df = pd.read_csv(filename, sep=',', header=0)
    list_nu.append(df)
    
sheet_nu = pd.concat(list_nu, axis=0, ignore_index=True)

#filtros


is_fatura = sheet_nu.loc[sheet_nu['Descrição'].str.contains("fatura", case=False)]
is_ganho = sheet_nu.loc[sheet_nu['Valor'] > 0]
x = sum(is_fatura['Valor'])
y = sum(is_ganho['Valor'])
print(x)
print(y)

#fazer template simples conseguindo filtrar pelo api. e mostrando na tela