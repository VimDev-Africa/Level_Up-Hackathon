from django.http import response
from rest_framework.views import APIView
from databased.models import Player

class Badge(APIView):
    # permission_classes = (IsAuthenticated,)
    def get(self, req):
        player = Player.objects.create(name="")
        player.save()
        return response(data = {}, status=response.HttpResponseBadRequest)

class user_reg(APIView):
    # permission_classes = (IsAuthenticated,)
    def post(self, req):
        
        pass