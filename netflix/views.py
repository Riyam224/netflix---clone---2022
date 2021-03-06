from cProfile import Profile
from re import L
from unicodedata import name
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
# Create your views here.
from .models import Profile , Movie

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import ProfileForm

class Home(View):
    def get(self , request , *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('netflix:ProfileList')
        return render(request , 'netflix/index.html' , {})

method_decorator(login_required , name='dispatch')
class ProfileList(View):
    def get(self, request , *args, **kwargs):
       
        profiles = request.user.profiles.all()
        context = {
            'profiles': profiles
        }
        return render(request , 'profileList.html' , context)



method_decorator(login_required , name='dispatch')
class ProfileCreate(View):
    def get(self, request , *args, **kwargs):
       
        form = ProfileForm()
       
        context = {
            'form': form
        }

        return render(request , 'profileCreate.html' , context) 


    def post(self, request , *args, **kwargs):
        form = ProfileForm(request.POST or None)
        if form.is_valid():
            profile = Profile.objects.create(**form.cleaned_data) 
            if profile:
                request.user.profiles.add(profile)
                return redirect('netflix:ProfileList')

        context = {
            'form': form
        }
        return render(request , 'profileCreate.html' , context)



# todo movie list for profile 

method_decorator(login_required , name='dispatch')
class MovieList(View):
    def get(self, request , profile_id, *args, **kwargs):

        try:
            profile = Profile.objects.get(uuid=profile_id)
            movies = Movie.objects.filter(age_limit=profile.age_limit)
            if profile not in request.user.profiles.all():
                return redirect('netflix:ProfileList')
                
            context = {
                'movies': movies
            }

            return render(request , 'movielist.html' , context)

        except Profile.DoesNotExist:
            return redirect('netflix:ProfileList')


# @login_required
# class MovieDetail(View):
#     def get(self, request ,movie_id, *args, **kwargs):
        
#         try:
#             movie = Movie.objects.get(uuid=movie_id)

#             context = {
#                 'movie': movie
#             }

#             return render(request , 'moviedetail.html' , context)

#         except Movie.DoesNotExist:
#             return redirect('netflix:ProfileList')

@login_required
def movie_detail(request , movie_id):
    movie = get_object_or_404(Movie , uuid=movie_id)
    context = {
        'movie': movie
    }

    return render(request , 'moviedetail.html', context)



def movie_play(request , movie_id):
    movie = get_object_or_404(Movie , uuid=movie_id)
    movie  =  movie.video.values()


    context = {
        'movie': list(movie)
    }

    return render(request , 'movieplay.html', context)
