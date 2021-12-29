from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from hubspot import HubSpot
from hubspot.auth.oauth import ApiException
from django.shortcuts import render, redirect
import json


file = open('hubspotAPI/config.json')

configs = json.load(file)

api_key  = configs['api_key']
redirect_uri = configs['redirect_uri']
client_id = configs['client_id']
client_secret = configs['client_secret']

file.close()

def index(request):
    if request.method == "GET":
        if request.session.get('token') != None:
            return render(request, 'index.html')

        else:
            installURL = 'https://app.hubspot.com/oauth/authorize?client_id=ab20ae3d-1be2-4ce2-803b-9e7ce2b6b526&redirect_uri=http://localhost:8000/auth&scope=crm.objects.contacts.read%20crm.objects.contacts.write%20crm.schemas.contacts.read%20crm.schemas.contacts.write'
            return redirect(installURL)

def auth(request):
    try:
        code = request.GET.get('code')

        api_client = HubSpot(api_key=api_key)

        tokens = api_client.auth.oauth.tokens_api.create_token(
            grant_type="authorization_code",
            redirect_uri=redirect_uri,
            client_id=client_id,
            client_secret=client_secret,
            code=code
        )

       # print(tokens.__getattribute__('acess_token'))
        token = tokens.access_token
        request.session['token'] = token
    
    except ApiException as ex:
        print('Exception when calling create_token method: {}\n'.format(ex))
        return redirect('logoff')
    
    return redirect('index')

def logoff(request):
    if request.method == "GET":
        request.session.clear()
        return redirect('index')