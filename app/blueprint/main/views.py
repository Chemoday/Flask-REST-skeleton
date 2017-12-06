from flask import render_template, session, \
    redirect, url_for, current_app, flash, request, make_response

from . import main_bp

@main_bp.route('/')
def index():
    return render_template('index.html')