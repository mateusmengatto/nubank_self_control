from search_data import *

def sum_expenses(data): #if data is filtered get filter function
    expenses = data.loc[data['Valor'] < 0]
    summed_expenses = sum(expenses['Valor'])