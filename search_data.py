import pandas as pd

class DataCompile: #receive pandas df
  def __init__(self, dataframe):
    self.data = dataframe
  

  def search_description(self, term):
    result_sheet = self.data.loc[self.data['Descrição'].str.contains(str(term), case = False)]
    return result_sheet.head()

#Converter data head 'Descriçao' para 'Description'
#criar classe de classificaçã

    