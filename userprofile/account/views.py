from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User
from .serializer import RegisterSerializer,UserSerializer
from rest_framework import generics, status


# Create your views here.

class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({'message': 'User registered Successfully.'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


