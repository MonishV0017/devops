import os
from flask import Flask
app=Flask(__name__)
@app.route('/')
def home():
        return "hello,devops"
if __name__=="__main__":
	port=int(os.getenv("flask_port",5000))
	app.run(host='0.0.0.0',port=port)