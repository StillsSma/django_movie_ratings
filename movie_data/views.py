from django.shortcuts import render
from movie_data.models import Movie, Rating, Rater
from django.db.models import Avg
# Create your views here.

def index_view(request):
    context = {
     "top_20_movies": "Top 20 Movies",
     "all_movies": "All Movies",
     "all_users": "All Users",
    }
    return render(request, "index.html", context)

def top_20_view(request):
    context = {

    "20_movies": Movie.objects.annotate(average= Avg('rating__rating')).order_by('-average')[:20]
    }                                            # WHY Does __ work here? What is it doing? 

    return render(request, "top_20.html", context)

def all_movies_view(request):
    context = {
    "all_movies": Movie.objects.order_by('movie_title'),

    }
    return render(request, "all_movies.html", context)

def all_users_view(request):
    context = {
    "all_users": Rater.objects.all()
    }

    return render(request, "all_users.html", context)

def movie_page_view(request, movie_id):
    context = {
    "movie" : Movie.objects.get(id=movie_id),
    "raters": Rating.objects.filter(movie=movie_id).order_by('rater')

    }
    return render(request, "movie_page.html", context)

def user_page_view(request, rater_id):
    context = {
    "rater" : Rater.objects.get(id=rater_id),
    "movies_rated": Rating.objects.filter(rater=rater_id).order_by('movie')
    }
    return render(request, "user_page.html", context)
