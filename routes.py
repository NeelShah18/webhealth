from flask import Flask, render_template, request, session, redirect, url_for
#from models import db, User, Place
from forms import SignupForm, LoginForm
import login as ln

app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI'] = # add your Heroku Postgres database URL here

app.secret_key = "development-key"

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/about")
def about():
  return render_template("about.html")

@app.route("/signup", methods=["GET", "POST"])
def signup():
  colours = ['Red', 'Blue', 'Black', 'Orange']
  if 'email' in session:
    return redirect(url_for('home'))

  form = SignupForm()

  if request.method == "POST":
    if form.validate() == False:
      return render_template('signup.html', form=form, colours=colours)
    else:
      signup_result = ln.singup(form.first_name.data, form.last_name.data, form.username.data, form.password.data, form.email.data)
      session['email'] = form.email.data
      return redirect(url_for('home'))

  elif request.method == "GET":
    return render_template('signup.html', form=form)

@app.route("/login", methods=["GET", "POST"])
def login():
  if 'email' in session:
    return redirect(url_for('home'))

  form = LoginForm()

  if request.method == "POST":
    if form.validate() == False:
      return render_template("login.html", form=form)
    else:
      email = form.email.data
      password = form.password.data

      login_result = ln.login(email, password)
      if login_result['flag'] == True:
          session['email'] = form.email.data
          return redirect(url_for('home'))
      else:
          return redirect(url_for('login'))

  elif request.method == 'GET':
    return render_template('login.html', form=form)

@app.route("/logout")
def logout():
  session.pop('email', None)
  return redirect(url_for('index'))

@app.route("/home", methods=["GET"])
def home():
  if 'email' not in session:
    return redirect(url_for('login'))

  elif request.method == 'GET':
    return render_template("home.html")

if __name__ == "__main__":
  app.run(debug=True)