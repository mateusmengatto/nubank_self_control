import pandas as pd



def do_math(datframe, function):
    df = datframe
    if function == 'input':
        x = df.loc[df['Valor'] > 0]
        input_sum = x['Valor'].values.sum()
        print(x)
        return input_sum



