from .common import AlbumSerializer
from genres.serializers.common import GenreSerializer
from comments.serializers.common import CommentSerializer
from artists.serializers.common import ArtistSerializer
from comments.serializers.populated import PopulatedCommentSerializer
from jwt_auth.serializers.common import UserSerializer # import the UserSerializer
from songs.serializers.common import SongSerializer


class PopulatedAlbumSerializer(AlbumSerializer):
    genres = GenreSerializer(many=True)
    comments = CommentSerializer(many=True)
    songs = SongSerializer(many=True)
    artist = ArtistSerializer()
    # comments = PopulatedCommentSerializer(many=True)
    owner = UserSerializer() # We populate the owner key with the UserSerializer