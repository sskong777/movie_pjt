from dataclasses import fields
from rest_framework import serializers
from django.contrib.auth import get_user_model
from community.models import Article
from movies.models import Movie
from movies.views import favorite_movie
from movies.serializers.movie import MovieSerializer

class ProfileSerializer(serializers.ModelSerializer):

    class ArticleSerializer(serializers.ModelSerializer):
        
        class Meta:
            model = Article
            fields = ('pk', 'title', 'content')
    
    ## 추가
    # class MovieSerialiser(serializers.ModelSerializer):
    #     class Meta:
    #         model = Movie
    #         fields = ('pk','title','overview','poster_path','genres')

    ## 추가(수정)
    favorite_movies = MovieSerializer(many=True)
    # favorite_movies = MovieSerialiser(many=True)
    like_articles = ArticleSerializer(many=True)
    articles = ArticleSerializer(many=True)
    
    class Meta:
        model = get_user_model()
        fields = ('pk', 'username', 'email', 'like_articles', 'articles','favorite_movies')




# class ProfileSerializer(serializers.ModelSerializer):

#     class ArticleSerializer(serializers.ModelSerializer):
        
#         class Meta:
#             model = Article
#             fields = ('pk', 'title','content',)

#     like_reviews = ReviewSerializer(many=True)
#     user_reviews = ReviewSerializer(many=True)

#     class Meta:
#         model = get_user_model()
#         fields = ('pk', 'username', 'like_reviews', 'user_reviews',)
# # 



# from rest_framework import serializers
# from django.contrib.auth import get_user_model


# User = get_user_model()

# class ProfileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('id', 'username', 'email')


# from rest_framework import serializers
# from django.contrib.auth import get_user_model
# from community.models import Review

# class ProfileSerializer(serializers.ModelSerializer):

#     class ReviewSerializer(serializers.ModelSerializer):
        
#         class Meta:
#             model = Review
#             fields = ('pk', 'movie_title','content','rank')

#     like_reviews = ReviewSerializer(many=True, read_only=True)
#     user_reviews = ReviewSerializer(many=True, read_only=True)

#     class Meta:
#         model = get_user_model()
#         fields = ('pk', 'username', 'like_reviews', 'user_reviews',)
