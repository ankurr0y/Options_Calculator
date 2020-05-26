import pandas as pd
from datetime import datetime

def extracthigh(filename):
   #print(filename)
   extension='csvs//'+filename
   df=pd.read_csv(extension)
   high=df['High']
   return high

def extractlow(filename):
   #print(filename)
   extension='csvs//'+filename
   df=pd.read_csv(extension)
   low=df['Low']
   return low

def extractdate(filename):
   #print(filename)
   extension='csvs//'+filename
   df=pd.read_csv(extension)
   date=df['Date']
   dates=(datetime.strptime(A, '%Y-%m-%d') for A in date)
   dates_string=[datetime.strftime(d, '%Y-%m-%d') for d in dates]
   ret_date=[]
   for d in dates_string:
       ret_date.append(datetime.strptime(d, '%Y-%m-%d'))
   return ret_date
