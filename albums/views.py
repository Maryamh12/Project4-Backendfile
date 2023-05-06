from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound
from django.db import IntegrityError

from .models import Album
from .serializers.common import AlbumSerializer
from .serializers.populated import PopulatedAlbumSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

# Create your views here.

class AlbumListView(APIView):

    
    
    def get(self, _request):
        # get everything from the shows table in the db
        albums= Album.objects.all()

        # run everything through the serializer
        serialized_albums = PopulatedAlbumSerializer(albums, many=True)

        # return the response and a status
        return Response(serialized_albums.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        permission_classes = (IsAuthenticatedOrReadOnly, )
        request.data["owner"] = request.user.id
        album_to_add = AlbumSerializer(data=request.data)
        try:
             album_to_add.is_valid()
             album_to_add.save()
             return Response(album_to_add.data, status=status.HTTP_201_CREATED)
        except IntegrityError as e:
              res = {
                        "detail": str(e)
                }
              return Response(res , status=status.HTTP_422_UNPROCESSABLE_ENTITY)



        

class AlbumDetailView(APIView):

    def get(self, _request, pk):

        try:

            album = Album.objects.get(pk=pk)
            serialized_album = AlbumSerializer(album)
            return Response(serialized_album.data, status=status.HTTP_200_OK)
        except Album.DoesNotExist:
            raise NotFound(detail="Can't find that show!")

    def get_album(self, pk):
        try:
            return Album.objects.get(pk=pk)

        except Album.DoesNotExist:

            raise NotFound(detail="Can't find that show!")

    def get(self, _request, pk):
        album = self.get_album(pk=pk)
        serialized_album = AlbumSerializer(album)

        return Response(serialized_album.data, status=status.HTTP_200_OK)

    # def put(self, request, pk):
    #     album =self.get_album(pk=pk)

    #     serialized_album = AlbumSerializer(album)
    #     return Response(serialized_album.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        album_to_edit = self.get_album(pk=pk)

        updated_album = AlbumSerializer(album_to_edit, data=request.data )
        try:
            updated_album.is_valid()
            updated_album.save()
            return Response(updated_album.data, status=status.HTTP_202_ACCEPTED)

        except AssertionError as e:
            return Response({"detail": str(e)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        
        except:
            res = {
                "detail": "Unprocessable Entity"
            }
            return Response(res, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    def delete(self, _request, pk):
        album_to_delete = self.get_album(pk=pk)
        album_to_delete.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        

