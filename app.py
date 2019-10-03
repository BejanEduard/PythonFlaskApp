from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
from datetime import datetime

app = Flask(__name__)

app.config["SECRET_KEY"] = "k4=idc)$t+hfuj@%7+kp_8p)lw7xgv+7$&ojxxutimll^87&k+"
# Mock data for post generation

posts = [
    {
        'author': "Chorey Schafer",
        'title': "My first blog post",
        'content': "This is my content",
        'date_posted': datetime.now()
    },
{
        'author': "Bejan Eduard ",
        'title': "My Second Blog Post",
        'content': "Some content.",
        'date_posted': datetime.now()
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/register', methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash("You have registered successfuly", 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title="Register", form=form)


@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "admin@yahoo.com" and form.password.data == 'password':
            flash("You have logged in successfully", 'success')
        else:
            flash("Something went wrong. Please check your email and password.", 'danger')
        return redirect(url_for('home'))
    return render_template('register.html', title="Register", form=form)


if __name__ == '__main__':
    app.run(debug=True)
