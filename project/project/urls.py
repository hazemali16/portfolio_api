"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import include, path
from django.contrib import admin

from api import views

from django.conf.urls.static import static
from project import settings


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', views.get_toke, name="get_toke"),
    
    path('admin/', admin.site.urls),
    
    path('hero/', views.HeroList.as_view(), name="hero"),
    path('hero-data/', views.Hero.as_view(), name="hero-data"),
    path('hero/<int:pk>', views.HeroDetail.as_view(), name="hero"),
    
    
    path('jobs/', views.JobsList.as_view(), name="jobs"),
    path('jobs-data/', views.Jobs.as_view(), name="jobs-data"),
    path('jobs/<int:pk>', views.JobsDetail.as_view(), name="jobs"),
    
    
    path('about/', views.AboutList.as_view(), name="about"),
    path('about-data/', views.About.as_view(), name="about-data"),
    path('about/<int:pk>', views.AboutDetail.as_view(), name="about"),
    
    
    path('projects/', views.ProjectsList.as_view(), name="projects"),
    path('projects-data/', views.Projects.as_view(), name="projects-data"),
    path('projects/<int:pk>', views.ProjectsDetail.as_view(), name="projects"),
    
    
    path('skills/', views.SkillsList.as_view(), name="skills"),
    path('skills-data/', views.Skills.as_view(), name="skills-data"),
    path('skills/<int:pk>', views.SkillsDetail.as_view(), name="skills"),
    
    
    path('messages/', views.MessagesList.as_view(), name="messages"),
    
    
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)