from flask import jsonify, request
from FilterAPI import app, db
from FilterAPI.models import Data


def find_data(inputData):
    if inputData['type'] == 'shoppingLine':
        return Data.shoppingLine().get_data()
    elif inputData['type'] == 'salesLine':
        return Data.salesLine().get_data()
    else:
        return jsonify(status='error')


@app.route('/status')
def first_page():
    return jsonify(status="ok")

@app.route('/allData')
def all_data():
    return (Data.getAll())

@app.route('/getData', methods=['POST'])
def get_data():
    result = find_data(request.form.to_dict())
    return (result)