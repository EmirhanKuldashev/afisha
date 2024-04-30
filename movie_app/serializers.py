from movie_app.models import Director, Movie, Review
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ['id', 'name']

class MovieSerializer(serializers.ModelSerializer):
    director = DirectorSerializer()

    class Meta:
        model = Movie
        fields = ['id', 'title', 'description', 'duration', 'director']

class ReviewSerializer(serializers.ModelSerializer):
    movie = MovieSerializer()

    class Meta:
        model = Review
        fields = ['id', 'text', 'stars', 'movie']

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

class MovieValidateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=250)
    description = serializers.CharField()
    duration = serializers.FloatField(min_value=2)
    director_id = serializers.IntegerField(min_value=1)

    def validate_director_id(self, director_id):
        try:
            Director.objects.get(id=director_id)
        except Director.DoesNotExist:
            raise ValidationError('Director not found')
        return director_id

class DirectorValidateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=250)



class ReviewValidateSerializer(serializers.Serializer):
    text = serializers.CharField()
    star = serializers.IntegerField(min_value=1, max_value=5)
    movie_id = serializers.IntegerField(min_value=1)

    def validate_movie_id(self, movie_id):
        try:
            Movie.objects.get(id=movie_id)
        except Director.DoesNotExist:
            raise ValidationError('Movie not found')
        return movie_id

class DirectorValidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ['name']

class MovieValidateSerializer(serializers.ModelSerializer):
    director_id = serializers.IntegerField(min_value=1)

    class Meta:
        model = Movie
        fields = ['title', 'description', 'duration', 'director_id']

    def validate_director_id(self, value):
        try:
            Director.objects.get(id=value)
        except Director.DoesNotExist:
            raise serializers.ValidationError('Director not found')
        return value

class ReviewValidateSerializer(serializers.ModelSerializer):
    movie_id = serializers.IntegerField(min_value=1)

    class Meta:
        model = Review
        fields = ['text', 'stars', 'movie_id']

    def validate_movie_id(self, value):
        try:
            Movie.objects.get(id=value)
        except Movie.DoesNotExist:
            raise serializers.ValidationError('Movie not found')
        return value