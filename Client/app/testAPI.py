import requests
import json

baseurl = 'http://app-karen-m.fandogh.cloud'

#baseurl for local network:
#baseurl = http://127.0.0.1:5000

def shoppingLine():
    data = {'type':'shoppingLine'}
    response = requests.post(baseurl+'/getData', data=data)
    return json.loads(response.text)

def allData():
    response = requests.get(baseurl+'/allData')
    return json.loads(response.text)

def salesLine():
    data = {'type':'salesLine'}
    response = requests.post(baseurl+'/getData', data=data)
    return json.loads(response.text)


#TODO esma bayad avaz beshan :)
print("all Data count: ", len(allData()))
print("salesLine count: ", len(salesLine()))
print("shoppingLine count: ", len(shoppingLine()))
