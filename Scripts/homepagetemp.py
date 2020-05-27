from flask import Flask,render_template,url_for,flash,request,redirect
from form_function import InfoForm
import pandas as pd
from extractor import extracthigh,extractlow,extractdate
from prediction_models import modelmin,modelmax
from pricing_formula import retrieve_price
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
        upvalue=modelmax(date,high)
        downvalue=modelmin(date,high)
        '''if csp>upvalue:
           flash('Current stock price is too high')
           form=InfoForm()
           return redirect(url_for('homepage'))
           #return render_template('Options_Calculator.html',form=form)
        if csp<downvalue:
           flash("Current stock price is too low")
           form=InfoForm()
           return redirect(url_for('homepage'))
           #return render_template('Options_Calculator.html',form=form)'''
        #print(upvalue)
        #print(downvalue)
        option_price=retrieve_price(csp,rfr,ep,upvalue,downvalue)
        #print(option_price)
        #print(high)
        #print(low)
        #print(date)
        #return render_template('index.html',form=form,filename=extract(filename))
        return render_template('result.html',price=option_price)

if __name__ == '__main__':
   app.run()
