from flask import flash, redirect, render_template
from microblog.app import app
from microblog.app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'TR33HGR'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Seoul!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avenger movies are overrated!'
        },
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login request for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)
