from flask_wtf import FlaskForm
from wtforms import FileField,TextField, IntegerField, TextAreaField, SubmitField, RadioField, SelectField, validators, ValidationError,FloatField

class InfoForm(FlaskForm):
    currentStockPrice=FloatField('Enter the current price of the stock',[validators.Required('Compulsory Field')])
    riskFreeRate=FloatField('Enter current risk free rate:',[validators.Required('Compulsory Field')])
    exercisePrice=FloatField('Enter exercise price:',[validators.Required('Compulsory Field')])
    file=FileField('Enter the csv file with stock information:',[validators.Required('Compulsory Field')])
    submit=SubmitField('Input this information')
