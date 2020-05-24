from flask import Flask,render_template,url_for,flash,request
from form_function import InfoForm
app=Flask(__name__)
app.secret_key = 'development key'
filename=''
@app.route('/',methods=['GET','POST'])
@app.route('/home/',methods=['GET','POST'])
def upload():
   return render_template('homepage.html')

@app.route('/next/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        f = request.files['file']
        f.save('templates/'+f.filename)
        print(type(f.filename))
        filename=f.filename
        print(filename)
        form=InfoForm()
        return render_template('index.html',form=form,filename=filename)

def getFileName():
   return filename
if __name__ == '__main__':
   app.run()
