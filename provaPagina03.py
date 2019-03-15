'''
Created on 13 mar 2019

@author: mpasteri

https://medium.freecodecamp.org/how-to-build-a-web-application-using-flask-and-deploy-it-to-the-cloud-3551c985e492
https://medium.freecodecamp.org/how-to-build-a-web-application-using-flask-and-deploy-it-to-the-cloud-3551c985e492

1)Important Point To Remember
The Flask Framework looks for HTML files in a folder called 
templates. 
You need to create a templates folder and put all your HTML files in there.

'''
from flask import Flask, render_template             

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/massimp")
def salvador():
    return "Hello, Massimp"

if __name__ == "__main__":
    app.run(debug=True)
  
