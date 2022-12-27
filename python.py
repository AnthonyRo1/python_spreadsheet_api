import pygsheets
import pandas as pd
#authorization
gc = pygsheets.authorize(service_file = '/home/anthoroot/personal_work/python_spreadsheet/creds.json')


# Create empty dataframe 
df = pd.DataFrame()

# create a column
df['name'] = ['John', 'Steve', 'Sarah']


# open the gogle spreadsheet where 'PY to Gsheet Test' is the name of my sheet)
sh = gc.open('Python Test Sheet')

# select the first sheet
wks = sh[0]

#update the first sheet with df, starting at cell B2.