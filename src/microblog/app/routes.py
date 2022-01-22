from flask import render_template
from microblog.app import app


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
