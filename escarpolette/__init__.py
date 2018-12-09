from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

from escarpolette.player import Player

app = Flask(__name__)
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///../db.sqlite"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
player = Player(app)

import escarpolette.api
