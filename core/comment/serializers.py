from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from core.abstract.serializers import AbstractSerializer
from core.user.models import User
from core.post.models import Post
from core.comment.models import Comment
from core.user.serializers import UserSerializer


class CommentSerializer(AbstractSerializer):
    author=serializers.SlugRelatedField(slug_field='public_id',queryset=User.objects.all())
    post=serializers.SlugRelatedField(slug_field='public_id',queryset=Post.objects.all())
    
    def to_representation(self, instance):
        rep=super().to_representation(instance)
        author=User.objects.get_object_by_public_id(rep['author'])
        rep['author']=UserSerializer(author).data
        return rep
    class Meta:
        model = Comment
        fields =['id','author','post','body','created','updated','edited']
        read_only_fields=['edited']