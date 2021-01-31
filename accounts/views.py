from rest_framework import generics

from .models import User
from .serializers import UserSerializer


class UserList(generics.ListCreateAPIView):
    """
        List all users or create a new user
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    """
        Retrieve, update or delete a users instance.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
