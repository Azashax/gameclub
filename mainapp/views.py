from django.shortcuts import render
from docutils.nodes import status
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import *
from .models import *
from gameclub.pagination import CustomPagination
from .models import *
from .serializers import *


# Create your views here.

# viewvset:

class DeviceViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Device.objects.all()
        serializers = DeviceSerializer(queryset, many=True)
        return Response(serializers.data)

    def post(self, request):
        serializers = DeviceSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    pagination_class = CustomPagination


class GamerViewSet(viewsets.ModelViewSet):
    queryset = Gamer.objects.all()
    serializer_class = GamerSerializer
    pagination_class = CustomPagination


class RentedDeviceViewSet(viewsets.ModelViewSet):
    queryset = RentedDevice.objects.all()
    serializer_class = RentedDeviceSerializer
    pagination_class = CustomPagination










# get
class BookCategoryListView(generics.ListAPIView):
    queryset = BookCategory.objects.all()
    serializer_class = BookCategorySerializer












# post
class BookCategoryCreateView(generics.CreateAPIView):
    queryset = BookCategory.objects.all()
    serializer_class = BookCategorySerializer


# get end post
class BookCategoryListCreateView(generics.ListCreateAPIView):
    queryset = BookCategory.objects.all()
    serializer_class = BookCategorySerializer


# get

class BookCategoryRetrieveView(generics.RetrieveAPIView):
    queryset = BookCategory.objects.all()
    serializer_class = BookCategorySerializer


# put
class BookCategoryUpdetaView(generics.UpdateAPIView):
    queryset = BookCategory.objects.all()
    serializer_class = BookCategorySerializer


# get ned put
class BookCategoryUpdetaRetrieveView(generics.RetrieveUpdateAPIView):
    queryset = BookCategory.objects.all()
    serializer_class = BookCategorySerializer

# delete
class BookCategoryDestroyView(generics.DestroyAPIView):
    queryset = BookCategory.objects.all()
    serializer_class = BookCategorySerializer