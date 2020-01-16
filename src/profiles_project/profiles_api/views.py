from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from . import serializers

# Create your views here.

class HelloApiView(APIView):
    """Test APIView"""

    serailizer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Return a list of APIViews."""

        an_apiview = [
            'Uses HTTP methods as function (get, post, put, patch, delete)',
            'It is similar to a traditional Django view',
            'Gives you the most control over your logic',
            'Is mapped mannualy to URLs'
        ]

        return Response({'message':'Hello!', 'an_apiview':an_apiview})

    def post(self, request):
        """Create a hello message with our name."""

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message':message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handle an update method."""

        return Response({'method':'Put'})

    def patch(self, request, pk=None):
        """Patch request, only update the fields provided in the request."""

        return Response({'method':'Patch'})

    def delete(self, request, pk=None):
        """Delete an object"""

        return Response({'method':'Delete'})

class HelloViewSet(viewsets.ViewSet):
    """Test API Viewset"""

    def list(self, request):
        """Return a hello message"""

        a_viewset = [
        'Uses actions (list, create, update, update partial, destroy)',
        'Automatically map to URLs using Routers',
        'Provide more functionality with less code'
        ]

        return Response({'message':'Hello', 'a_viewset':a_viewset})
