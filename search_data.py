import pandas as pd
import datetime as dt

def search_description(data, term):
  result_sheet = data.loc[data['Descrição'].str.contains(str(term), case = False)] 
  return result_sheet

def search_identificator(data, term):
  result_sheet = data.loc[data['Identificador'].str.contains(str(term), case = False)]
  return result_sheet
    
def search_date(data, term):
  result_sheet = data.loc[data['Data'].str.contains(str(term), case = False)]
  return result_sheet

def search_period(data, start_time, end_time): #Rever problema de função
  data['Data'] = pd.to_datetime(data['Data'], format = "%d/%m/%Y")
  period = data[pd.date_range(start_time, end_time)]
  return period

def search_send_pix(data):
  term = 'enviada pelo Pix'
  result_sheet = data.loc[data['Descrição'].str.contains(str(term), case = False)]
  return result_sheet

def search_receive_pix(data):
  term = 'recebida pelo Pix'
  result_sheet = data.loc[data['Descrição'].str.contains(str(term), case = False)]
  return result_sheet


#code will be modified by language