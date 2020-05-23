from flask import Flask,render_template,url_for,flash,request
from form_function import InfoForm
app=Flask(__name__)
app.secret_key = 'development key'

@app.route('/',methods=['GET','POST'])
@app.route('/home/',methods=['GET','POST'])
def upload():
   return render_template('homepage.html')

@app.route('/next/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        f = request.files['file']
        f.save('templates/'+f.filename)
        print(f.filename)
        form=InfoForm()
        return render_template('index.html',form=form)

    
if __name__ == '__main__':
   app.run()
