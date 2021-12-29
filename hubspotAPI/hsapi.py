import requests
import json


file = open('hubspotAPI/config.json')

configs = json.load(file)

 
APIKEY_VALUE = configs['api_key']

file.close()

APIKEY = '?hapikey=' + APIKEY_VALUE

HS_API_URL = 'https://api.hubapi.com'



def creatOrUpdateContact(data):
    xurl = '/contacts/v1/contact/createOrUpdate/email/'+data['email']+'/'

    endpoint  = HS_API_URL + xurl + APIKEY
    headers = {}
    headers['Content-Type']= 'application/json'

    dataAux = json.dumps({
        "properties": [
            {
            "property": "email",
            "value": data['email']
            },  
            {
            "property": "phone",
            "value": data['phone']
            },    
            {
            "property": "date_of_birth",
            "value": data['date_of_birth']
            },
            {
            "property": "peso",
            "value": data['peso']
            }
        ]
    })

    r = requests.post( url = endpoint , data = dataAux, headers = headers )

    return r.status_code


def getTotalNumberOfContacts():
    xurl = '/contacts/v1/contacts/statistics'

    url = HS_API_URL + xurl + APIKEY

    response = requests.get(url).read()

    statistics = json.loads(response)

    return statistics['contacts']

#print(getTotalNumberOfContacts())
#print(creatOrUpdateContact('teste6@gmail.com'))
