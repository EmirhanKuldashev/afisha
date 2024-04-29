from movie_app.models import Director, Movie, Review
from rest_framework import serializers

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
    director = DirectorSerializer()

    class Meta:
        model = Movie
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    movie = MovieSerializer()

    class Meta:
        model = Review
        fields = ['text', 'stars']

class MovieReviewSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True)
    rating = serializers.SerializerMethodField()

    def get_rating(self, movie):
        reviews = Review.all
        total_stars = sum([review.stars for review in reviews])
        if reviews.count() > 0:
            return total_stars / reviews.count()
        else:
            return 0

    class Meta:
        model = Movie
        fields = ['title', 'description', 'duration', 'director', 'reviews', 'rating']

class DirectorWithMoviesCountSerializer(serializers.ModelSerializer):
    movies_count = serializers.SerializerMethodField()

    def get_movies_count(self, movie):
        return movie.all().count()

    class Meta:
        model = Director
        fields = ['name', 'movies_count']

