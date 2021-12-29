from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from hubspot import HubSpot
from hubspot.crm.contacts import SimplePublicObjectInput
from hubspot.crm.contacts.exceptions import ApiException
from ..hsapi import creatOrUpdateContact


class ContactViews(APIView):
    def post(self, request):
        token = request.session.get('token')

        try: 
            authenticated_api_client = HubSpot()  
            authenticated_api_client.access_token = token

            simple_public_object_input = SimplePublicObjectInput(
                properties=request.data
             )

            api_response = authenticated_api_client.crm.contacts.basic_api.create( 
                simple_public_object_input=simple_public_object_input
            )

            print(api_response)
        except ApiException as ex:
            if ex.status == status.HTTP_401_UNAUTHORIZED:
                return Response({"status":"error", "reason": ex.reason, "message": ex.body}, status=status.HTTP_401_UNAUTHORIZED)

            if ex.status == status.HTTP_409_CONFLICT:
                if creatOrUpdateContact(request.data) == status.HTTP_200_OK:
                    return Response({"status":"success"},  status.HTTP_201_CREATED)
                else: 
                    Response({"status":"error"}, status=status.HTTP_409_CONFLICT)
        
        return Response({"status":"success"}, status=status.HTTP_200_OK)
