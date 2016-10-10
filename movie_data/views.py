from django.shortcuts import render
from movie_data.models import Movie, Rating
# Create your views here.

def index_view(request):
    context = {
     "top_20_movies": "Top 20 Movies",
     "all_movies": "All Movies",
     "all_users": "All Users",
    }
    return render(request, "index.html", context)

def show_view(request):
    context = {
    "thing": Rating.ave_rating()
    }

    return render(request, "show.html", context)
