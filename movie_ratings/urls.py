"""movie_ratings URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from movie_data.views import index_view, top_20_view, all_movies_view, movie_page_view, all_users_view, user_page_view


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index_view),
    url(r'^movie/1/$', top_20_view),
    url(r'^movie/2/$', all_movies_view),
    url(r'^movie_info/(?P<movie_id>\d+)/$', movie_page_view),
    url(r'^movie/3/$', all_users_view),
    url(r'^user_info/(?P<user_id>\d+)/$', user_page_view),



]
