from rest_framework import serializers
from .models import contacts,user
from django.contrib.auth.models import User

class ContactListDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = contacts
        fields = '__all__'


class UserListDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = '__all__'