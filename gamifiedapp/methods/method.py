from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from databased.models import Player
from databased.serialerzers import PlayerSerializer


class Badge(APIView):
    # permission_classes = (IsAuthenticated,)
    def get(self, req):
        
        return Response(data = {"got a badge"}, status=HTTP_200_OK)

class User_reg(APIView):
    # permission_classes = (IsAuthenticated,)
    def post(self, req):
        user_info = req.data
        serialized = PlayerSerializer(data=user_info)
        
        if serialized.is_valid():
            serialized.save()
            return Response(data =user_info, status=HTTP_200_OK)
        else:
            return Response(data =user_info, status=HTTP_400_BAD_REQUEST)
        
        
        
        # jsonObject = PlayerSerializer(data=Player.objects.create())

    
    
class Login(APIView):
    def post (self, req):
        return Response(data = {"logged"}, status=HTTP_200_OK)


class Objective(APIView):
    
    def get(self, req):
        
        return Response(data = {'objective'}, status=HTTP_200_OK)
    
