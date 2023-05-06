from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers.populated import PopulatedGenreSerializer
from .serializers.common import GenreSerializer
from .models import Genre
from django.db import IntegrityError

# Create your views here.

class GenreListView(APIView):
    def get(self, _request):
        genres = Genre.objects.all()
        serialized_genres = PopulatedGenreSerializer(genres, many=True)
        return Response(serialized_genres.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        genre_to_add = GenreSerializer(data=request.data)
        try:
             genre_to_add.is_valid()
             genre_to_add.save()
             return Response(genre_to_add.data, status=status.HTTP_201_CREATED)
        except IntegrityError as e:
              res = {
                        "detail": str(e)
                }
              return Response(res , status=status.HTTP_422_UNPROCESSABLE_ENTITY)



