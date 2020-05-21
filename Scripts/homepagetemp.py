from flask import Flask,render_template,url_for,flash,request
from form_function import InfoForm
app=Flask(__name__)
app.secret_key = 'development key'

@app.route('/',methods=['GET','POST'])
def index():
    form=InfoForm()
    return render_template('index.html',form=form)

@app.route('/calculation/',methods=['GET','POST'])
def printout():
    print(7)
    
if __name__ == '__main__':
   app.run()
