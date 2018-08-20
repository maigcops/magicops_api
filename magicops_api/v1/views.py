from rest_framework import viewsets
from django.contrib.auth.models import User, Group
from magicops_api.v1 import serializers


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewd or edited.
    """

    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = serializers.UserSerializer
    lookup_field = 'username'


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewd or edited.
    """
    queryset = Group.objects.all()
    serializer_class = serializers.GroupSerializer
