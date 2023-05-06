from .common import SongSerializer
from albums.serializers.common import AlbumSerializer



class PopulatedSongSerializer(SongSerializer):
    album = AlbumSerializer()
    