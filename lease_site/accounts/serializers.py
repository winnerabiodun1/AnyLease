from rest_framework import serializers
from .models import Customer

class CustomerSerializer(serializers.Serializer):

    class Meta:
        model = Customer
        fields = "__all__"

    def create(self, validated_data):
        return Customer.objects.create(**validated_data)