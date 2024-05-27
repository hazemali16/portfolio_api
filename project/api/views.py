from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.authtoken.models import Token
from rest_framework.pagination import PageNumberPagination
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .serializers import *
from .models import *

class HeroList(generics.ListCreateAPIView):
    parser_classes = (FormParser,MultiPartParser, JSONParser)
    queryset = Hero.objects.all().order_by('-id')
    serializer_class = HeroSerializer

class HeroDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hero.objects.all()
    serializer_class = HeroSerializer

class JobsList(generics.ListCreateAPIView):
    queryset = Job.objects.all().order_by('-id')
    serializer_class = JobSerializer

class JobsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

class AboutList(generics.ListCreateAPIView):
    parser_classes = (FormParser,MultiPartParser, JSONParser)
    queryset = About.objects.all().order_by('-id')
    serializer_class = AboutSerializer

class AboutDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer

class SkillsList(generics.ListCreateAPIView):
    parser_classes = (FormParser,MultiPartParser, JSONParser)
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

class SkillsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

class ProjectsList(generics.ListCreateAPIView):
    parser_classes = (FormParser,MultiPartParser, JSONParser)
    queryset = Project.objects.all().order_by('-id')
    serializer_class = ProjectSerializer

class ProjectsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

@permission_classes((AllowAny,))
class MessagesList(generics.ListCreateAPIView):
    queryset = Message.objects.all().order_by('-id')
    serializer_class = MessageSerializer


@permission_classes((AllowAny,))
class Hero(generics.ListAPIView):
    queryset = Hero.objects.all().order_by('-id')
    serializer_class = HeroSerializer

@permission_classes((AllowAny,))
class Jobs(generics.ListAPIView):
    queryset = Job.objects.all().order_by('-id')
    serializer_class = JobSerializer

@permission_classes((AllowAny,))
class About(generics.ListAPIView):
    queryset = About.objects.all().order_by('-id')
    serializer_class = AboutSerializer

@permission_classes((AllowAny,))
class Skills(generics.ListAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

@permission_classes((AllowAny,))
class Projects(generics.ListAPIView):
    queryset = Project.objects.all().order_by('-id')
    serializer_class = ProjectSerializer

@api_view(['POST'])
@permission_classes((AllowAny,))
def get_toke(request) :
    username = request.data['username']
    password = request.data['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        # user = User.objects.get(username=username)
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})
    else :
        return Response({'error': 'wrong password or username'})
