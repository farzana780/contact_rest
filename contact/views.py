from django.http import JsonResponse
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from contact.models import Contact_data
from contact.serializers import  UserSerializer,ContactSerializer



class Home(APIView):
    def get(self, request, format=None):
        user_data = Contact_data.objects.all()
        user_serializer = UserSerializer(user_data, many=True)
        return JsonResponse({"user": user_serializer.data})

    def post(self, request, formate=None):
        user_data = JSONParser().parse(request)
        user_serializer = ContactSerializer(data=user_data)
        user_serializer.is_valid(raise_exception=True)
        user_serializer.save()
        return JsonResponse(user_serializer.data, status=status.HTTP_201_CREATED)

