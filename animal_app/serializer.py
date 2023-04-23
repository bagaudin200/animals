from rest_framework import serializers
from .models import Animal

class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = '__all__'

class CreateAnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = '__all__'

class UpdateAnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = '__all__'