# path(route, view, name):

# route: the URL pattern (string)

# view: the function or class that handles requests

# name: optional, useful for reverse URL lookups

from django.urls import path
from . import views

urlpatterns =[
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('portfolio/',views.portfolio,name='portfolio'),
    path('contact/',views.contact,name='contact'),
    path('blog/',views.blog,name='blog'),
]