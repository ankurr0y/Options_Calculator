from flask import Flask,render_template,url_for,flash,request
from form_function import InfoForm
import pandas as pd
from extractor import extracthigh,extractlow,extractdate

app=Flask(__name__)
app.secret_key = 'development key'
filename=''
'''def extract(filename):
   print(filename)
   extension='templates//'+filename
   df=pd.read_csv(extension)
   high=df['High']
   return high'''
@app.route('/',methods=['GET','POST'])
@app.route('/home/',methods=['GET','POST'])
def homepage():
   form=InfoForm()
   return render_template('Options_Calculator.html',form=form)
'''def upload():
   return render_template('homepage.html')'''

@app.route('/next/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        f = request.files['file']
        a=request.form
        for A,B in a.items():
           if A=='currentStockPrice':
              csp=float(B)
           elif A== 'riskFreeRate':
              rfr=float(B)
           elif A=='exercisePrice':
              ep=float(B)
        #print(type(csp))
        #print(csp)
        #print(rfr)
        #print(ep)
        f.save('csvs/'+f.filename)
        #print(type(f.filename))
        filename=f.filename
        high=extracthigh(filename)
        low=extractlow(filename)
        date=extractdate(filename)
        print(high)
        print(low)
        print(date)
        #return render_template('index.html',form=form,filename=extract(filename))
        return render_template('404.html')

if __name__ == '__main__':
   app.run()
