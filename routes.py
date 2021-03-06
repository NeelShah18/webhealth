#https://www.cdc.gov/diabetes/diabetesatwork/plan/costs.html
#http://www.diabetes.org/diabetes-basics/statistics/infographics/adv-staggering-cost-of-diabetes.html
#http://www.diabetes.org/diabetes-basics/statistics/infographics/adv-staggering-cost-of-diabetes.html
from flask import Flask, render_template, request, session, redirect, url_for
#from models import db, User, Place
from forms import SignupForm, LoginForm, ForgotForm
import login as ln
import getme as gm

app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI'] = # add your Heroku Postgres database URL here

app.secret_key = "development-key"

@app.route("/")
def index():
      if 'email' in session:
            return redirect(url_for('home'))
      else:
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
        print("here-->1")
        return render_template('signup.html', form=form)
    else:
        signup_result = ln.singup(form.first_name.data, form.last_name.data, form.username.data, form.password.data, form.email.data, form.food.data, form.exer.data)
        session['email'] = form.email.data
        return redirect(url_for('home'))

  elif request.method == "GET":
     print("here-->3")
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

@app.route("/forgot", methods=["GET", "POST"])
def forgot():
  if 'email' in session:
    return redirect(url_for('home'))

  form = ForgotForm()

  if request.method == "POST":
    if form.validate() == False:
      return render_template("forgot.html", form=form)
    else:
      email = form.email.data
      password = form.password.data

      login_result = ln.update(email, password)
      if login_result['flag'] == True:
          return redirect(url_for('login'))
      else:
          return redirect(url_for('forgot'))

  elif request.method == 'GET':
    return render_template('forgot.html', form=form)

@app.route("/logout")
def logout():
  session.pop('email', None)
  return redirect(url_for('index'))

@app.route("/home", methods=["GET"])
def home():
  #print(session['email'])
  if 'email' not in session:
    return redirect(url_for('login'))

  elif request.method == 'GET':
    #print(session['email'])
    return render_template("main.html", email=str(session['email']), name=gm.get_name(session['email']), facebook="7 Millions", twitter="7.5 Millions", diabetes_per=gm.get_per(session['email']),medical_cost=gm.get_money(session['email']), line_graph=gm.line_value(session['email']))

if __name__ == "__main__":
    app.run(debug=True)
