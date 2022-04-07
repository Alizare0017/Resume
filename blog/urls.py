from unicodedata import name
from xml.etree.ElementInclude import include
from django.urls import path,include
from blog.views import *

app_name = 'blog'

urlpatterns = [
    path('',index_view),
    path('about',about_view,name='about'),
    path('home',index_view,name='home'),
    path('contact',contact_view,name='contact'),
    path('services',services_view,name='services'),
]