from rest_framework import serializers
from .models import ContractModal


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContractModal
        fields = ["name", "title", "email"]
