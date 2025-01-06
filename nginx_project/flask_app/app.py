from flask import Flask

app = Flask(__name__)

@app.route('/hello/<name>')

def hello_name(name):
	return f'Hello {name}!'

if __name == '__main__':
	app.run(host='0.0.0.0', port=5000)
