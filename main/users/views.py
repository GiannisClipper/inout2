from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


def signup(req):
    return HttpResponse('signup response', content_type="text/plain")


class Retrieve(APIView):

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, req, id):
        return HttpResponse(f'record {id}', content_type="text/plain")