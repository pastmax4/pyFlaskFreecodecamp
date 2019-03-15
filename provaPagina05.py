'''
Created on 13 mar 2019

@author: mpasteri

https://medium.freecodecamp.org/how-to-build-a-web-application-using-flask-and-deploy-it-to-the-cloud-3551c985e492
https://medium.freecodecamp.org/how-to-build-a-web-application-using-flask-and-deploy-it-to-the-cloud-3551c985e492

1)Important Point To Remember
The Flask Framework looks for HTML files in a folder called 
templates. 
You need to create a templates folder and put all your HTML files in there.
I files HTML sono tutti nella dir template

2)An important note to remember
In the same way as we created a folder called templates to store all our 
HTML templates, we need a folder called static.

In static, we will store our CSS, JavaScript, images, and other 
necessary files. That is why it is important that you should create a CSS 
folder to store your stylesheets.
'''

from flask import Flask, render_template             

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("template.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/massimp")
def massimp():
    return "Hello, Massimp"

if __name__ == "__main__":
    app.run(debug=True)
  
  
