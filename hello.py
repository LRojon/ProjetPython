from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
	return '<h1>Hello World !!</h1>'
    
@app.route('/john')
def vntm():
	return '<h3> vntm :) </h3>'

	

