from .common import GenreSerializer
from albums.serializers.common import AlbumSerializer


class PopulatedGenreSerializer(GenreSerializer):
    albums = AlbumSerializer(many=True)