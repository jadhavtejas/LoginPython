from rest_framework import serializers


class Contact(serializers.Serializer):
    Username = serializers.CharField(max_length=100)
    Email = serializers.CharField(max_length=100)
    Query = serializers.CharField(max_length=100)