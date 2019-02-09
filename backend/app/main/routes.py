from datetime import datetime
from flask import render_template, flash, redirect, url_for, request
from app.main import bp

@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET', 'POST'])
def index():
    return "Hello World!"

