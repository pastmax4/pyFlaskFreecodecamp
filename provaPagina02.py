'''
Created on 13 mar 2019

@author: mpasteri

https://medium.freecodecamp.org/how-to-build-a-web-application-using-flask-and-deploy-it-to-the-cloud-3551c985e492
https://medium.freecodecamp.org/how-to-build-a-web-application-using-flask-and-deploy-it-to-the-cloud-3551c985e492

Important Point To Remember


'''

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World!"
    
@app.route("/massimp")
def massimp():
    return "Hello, Massimp"

if __name__ == "__main__":
    app.run(debug=True)
