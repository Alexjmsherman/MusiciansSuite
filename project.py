from flask import Flask, render_template, request, redirect, \
    url_for, flash, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import user
from database import Base


app = Flask(__name__)

engine = create_engine('sqlite:///metronome.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')
def Home():
    person = user.User()
    person.update_total()
    return str(person.total)

if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
