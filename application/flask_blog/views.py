from flask_blog import app
from flask import render_template, redirect, request, url_for,  flash, session


@app.route('/')
def show_entries():
    return render_template('entries/index.html')