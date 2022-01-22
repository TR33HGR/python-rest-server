from flask import Flask
from microblog.config import Config

app = Flask(__name__)
app.config.from_object(Config)

from microblog.app import routes
