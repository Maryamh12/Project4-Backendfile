from .common import CommentSerializer
from albums.serializers.common import AlbumSerializer
from jwt_auth.serializers.common import UserSerializer


class PopulatedCommentSerializer(CommentSerializer):
    album = AlbumSerializer()
    owner = UserSerializer()