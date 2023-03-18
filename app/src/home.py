from flask import jsonify, abort, render_template


def index():
    return render_template('index.html')
