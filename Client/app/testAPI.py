import requests
import json

def shoppingLine():
    data = {'type':'shoppingLine'}
    response = requests.post('http://0.0.0.0:5000/getData', data=data)
    return json.loads(response.text)

def allData():
    response = requests.get('http://0.0.0.0:5000/allData')
    return json.loads(response.text)

def salesLine():
    data = {'type':'salesLine'}
    response = requests.post('http://0.0.0.0:5000/getData', data=data)
    return json.loads(response.text)


#TODO esma bayad avaz beshan :)
print("all Data count: ", len(allData()))
print("salesLine count: ", len(salesLine()))
print("shoppingLine count: ", len(shoppingLine()))