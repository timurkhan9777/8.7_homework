from django.shortcuts import render
from .models import Category,Comment,Header,Navbar,Travel,Description
from .serializers import (CategorySerializers,CommentSerializers,HeaderSerializers,NavbarSerializers,
                          TravelSerializers,DescriptionSerializers)
from rest_framework.viewsets import ModelViewSet
from .permissions import CustomPermission

class CategoryAPIView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
    permission_classes = [CustomPermission]

class HeaderAPIView(ModelViewSet):
    queryset = Header.objects.all()
    serializer_class = HeaderSerializers
    permission_classes = [CustomPermission]

class NavbarAPIView(ModelViewSet):
    queryset = Navbar.objects.all()
    serializer_class = NavbarSerializers
    permission_classes = [CustomPermission]

class TravelAPIView(ModelViewSet):
    queryset = Travel.objects.all()
    serializer_class = TravelSerializers
    permission_classes = [CustomPermission]

class CommentAPIView(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializers
    permission_classes = [CustomPermission]


class DescriptionAPIView(ModelViewSet):
    queryset = Description.objects.all()
    serializer_class = DescriptionSerializers