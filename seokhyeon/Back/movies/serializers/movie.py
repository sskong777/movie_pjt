from email.policy import default
from ..models import Actor, Movie
from ..models import Genre
from ..models import Review
from rest_framework import serializers
from django.contrib.auth import get_user_model


class ActorSerializer(serializers.ModelSerializer):
    class MovieListSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('pk', 'poster_path', 'title')
    movies = MovieListSerializer(many=True, read_only=True)
    class Meta:
        model = Actor
        fields = '__all__'
        read_only_fields = ('movies',)

# Genre Serializer
class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('name',)


# Review Serializer
User = get_user_model()

class ReviewSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username')

    user = UserSerializer(read_only=True)

    class Meta:
        model = Review
        fields = ('pk', 'user', 'content', 'movie', 'title', 'rank', 'created_at', 'updated_at')
        read_only_fields = ('movie', )

# Movie Serializers
class MovieListSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):

        class Meta:
            model = User
            fields = ('pk', 'username')

    favorite_count = serializers.IntegerField(default=0)
    reviews_rank_avg = serializers.FloatField(default=0)
    reviews = ReviewSerializer(many=True, read_only=True)
    genres = GenreSerializer(many=True, read_only=True)
    actors = ActorSerializer(many=True, read_only=True)
    user = UserSerializer(read_only=True)
    class Meta:
        model = Movie
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):

    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username')

    user = UserSerializer(read_only=True)
    reviews = ReviewSerializer(many=True, read_only=True)
    genres = GenreSerializer(many=True, read_only=True)
    actors = ActorSerializer(many=True, read_only=True)
    # movies/views.py => movie_detail에서 annotate로 추가
    reviews_rank_avg = serializers.FloatField(default=0)
    class Meta:
        model = Movie
        fields = '__all__'



#다시 수정해야함
# Favorite 
# class FavoriteListSerializer(serializers.ModelSerializer):
#     class UserSerializer(serializers.ModelSerializer):

#         class Meta:
#             model = User
#             fields = ('pk', 'username')

#     # reviews = ReviewSerializer(many=True, read_only=True)
#     genres = GenreSerializer(many=True, read_only=True)
#     # user = UserSerializer(read_only=True)
#     # queryset annotate 사용
#     # favorite_count = serializers.IntegerField()
#     class Meta:
#         model = Movie
#         fields = '__all__'