import imp
from unicodedata import name
from django.urls import path
from . import views



app_name = 'netflix'


urlpatterns = [
    path('' , views.Home.as_view() , name='Home'),
    path('profiles/' , views.ProfileList.as_view() , name='ProfileList'),
    path('profilecreate/' , views.ProfileCreate.as_view() , name='ProfileCreate'),

    path('watch/<str:profile_id>/' , views.MovieList.as_view() , name='MovieList'),
]
