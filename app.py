from flask import Flask,redirect

from resources.phoneNumProcessor import phone_api

DEBUG = True
HOST = '0.0.0.0'
PORT = 8000

app = Flask(__name__)
app.register_blueprint(phone_api)

@app.route('/')
def hello_world():
	return redirect('/static/phoneEntry.html', code=302)
			

if __name__ == '__main__':
	app.run(debug=DEBUG, host=HOST, port=PORT)

