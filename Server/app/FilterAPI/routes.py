from flask import jsonify
from FilterAPI import app, db
from FilterAPI.models import Data


@app.route('/status')
def first_page():
    return jsonify(status="ok")
