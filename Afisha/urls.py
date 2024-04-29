from django.contrib import admin
from django.urls import path
from movie_app.views import director_list,director_detail,review_detail,review_list,movie_list,movie_detail, movies_reviews_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/directors/', director_list, name='director-list'),
    path('api/v1/directors/<int:pk>/', director_detail, name='director-detail'),
    path('api/v1/movies/', movie_list, name='movie-list'),
    path('api/v1/movies/<int:pk>/', movie_detail, name='movie-detail'),
    path('api/v1/reviews/', review_list, name='review-list'),
    path('api/v1/reviews/<int:pk>/', review_detail, name='review-detail'),
    path('api/v1/movies/reviews/', movies_reviews_view, name='movies-reviews'),
]
