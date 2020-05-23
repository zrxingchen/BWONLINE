from django.shortcuts import render
from .models import UserProfile
from apps.users.serializers import UserProfileSerializers

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import viewsets
@api_view(['GET'])
def api_root(request,format=None):
    return Response({
        'users':reverse('user-list',request=request,format=format)
    })


class UserProfileViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializers

    # permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)