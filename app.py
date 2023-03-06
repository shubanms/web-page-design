#app.py
from flask import Flask,render_template
from forms import RegistrationForm,LoginForm

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('personal.html')
 
@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html' , title="Register",form = form)

if __name__ == "__main__":
    app.run()