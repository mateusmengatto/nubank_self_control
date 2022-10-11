import pandas as pd
import glob
import os

def open_data(path):
  csv_files = glob.glob(os.path.join(path, "*.csv"))

  list_nu = []

  for file in csv_files:
      df = pd.read_csv(file, sep=',', header = 0)
      list_nu.append(df)

  sheet_nu = pd.concat(list_nu, axis = 0, ignore_index = True)
  return sheet_nu