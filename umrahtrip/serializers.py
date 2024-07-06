from rest_framework import serializers
from .models import Category,Comment,Header,Navbar,Travel,Description

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class CommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class HeaderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Header
        fields = '__all__'

class NavbarSerializers(serializers.ModelSerializer):
    class Meta:
        model = Navbar
        fields = '__all__'

class TravelSerializers(serializers.ModelSerializer):
    class Meta:
        model = Travel
        fields = '__all__'

class DescriptionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Description
        fields = '__all__'