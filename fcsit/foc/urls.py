from django.urls import path
from .import views
urlpatterns = [
    path('index', views.home,name='home'),
    path('about', views.about,name='about'),
    path('teachers', views.teachers,name='teachers'),
    path('contact', views.contact,name='contact'),
    
]
