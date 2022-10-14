import pandas as pd
import datetime as dt

def search_description(data, term):
  result_sheet = data.loc[data['Descrição'].str.contains(str(term), case = False)] 
  return result_sheet

def search_identificator(data, term):
  result_sheet = data.loc[data['Identificador'].str.contains(str(term), 
                                                             case = False)]
  return result_sheet
    
def search_date(data, date):
  data['Data'] = pd.to_datetime(data['Data'], format = "%d/%m/%Y")
  result_sheet = data.loc[data['Data'] == date]
  return result_sheet

def search_period(data, start_time, end_time): 
  data['Data'] = pd.to_datetime(data['Data'], format = "%d/%m/%Y")
  filtered_period_data = data.loc[(data['Data'] >= start_time) 
                                  & (data['Data'] <= end_time)]
  return filtered_period_data

def search_send_pix(data):
  term = 'enviada pelo Pix'
  result_sheet = data.loc[data['Descrição'].str.contains(str(term), 
                                                         case = False)]
  return result_sheet

def search_receive_pix(data):
  term = 'recebida pelo Pix'
  result_sheet = data.loc[data['Descrição'].str.contains(str(term), 
                                                         case = False)]
  return result_sheet


#code will be modified by language