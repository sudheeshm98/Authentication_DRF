from django.shortcuts import render
from rest_framework.response import Response
from .models import User
from .serializer import RegisterSerializer,UserSerializer
from rest_framework import generics

# Create your views here.

class RegisterView(generics.CreateAPIView):
    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token,created = Token.object.get_or_create(user=user)
            return Response(status=status)


