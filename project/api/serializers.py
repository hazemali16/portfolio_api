from django.contrib.auth.models import Group, User
from rest_framework import serializers
from .models import *

class HeroSerializer(serializers.ModelSerializer):
    image = serializers.FileField(required=False)
    image_name = serializers.CharField(required=False)
    image_size = serializers.CharField(required=False)
    image_type = serializers.CharField(required=False)
    class Meta:
        model = Hero
        fields = '__all__'

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'


class AboutSerializer(serializers.ModelSerializer):
    image = serializers.FileField(required=False)
    image_name = serializers.CharField(required=False)
    image_size = serializers.CharField(required=False)
    image_type = serializers.CharField(required=False)
    class Meta:
        model = About
        fields = '__all__'

class SkillSerializer(serializers.ModelSerializer):
    image = serializers.FileField(required=False)
    image_name = serializers.CharField(required=False)
    image_size = serializers.CharField(required=False)
    image_type = serializers.CharField(required=False)
    class Meta:
        model = Skill
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    image = serializers.FileField(required=False)
    image_name = serializers.CharField(required=False)
    image_size = serializers.CharField(required=False)
    image_type = serializers.CharField(required=False)
    class Meta:
        model = Project
        fields = '__all__'

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'

