from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView
from databased.models import Player

class Badge(APIView):
    # permission_classes = (IsAuthenticated,)
    def get(self, req):
        player = Player.objects.create(name="")
        player.save()
        return Response(data = {}, status=HTTP_200_OK)

class user_reg(APIView):
    # permission_classes = (IsAuthenticated,)
    def post(self, req):
        
        pass