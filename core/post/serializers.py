from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from core.abstract.serializers import AbstractSerializer
from core.post.models import Post
from core.user.models import User
from core.user.serializers import UserSerializer

class PostSerializer(AbstractSerializer):
    author=serializers.SlugRelatedField(slug_field='public_id',queryset=User.objects.all())
    
    
    def validated_author(self, value):
        if self.context["request"].user != value:
            raise ValidationError("You can't create a post for another user")
        return value
    class Meta:
        model = Post
        fields = ['id','author','body','created','updated','edited']

    
    def to_representation(self, instance):
        rep=super().to_representation(instance)
        author=User.objects.get_object_by_public_id(rep['author'])
        rep['author']=UserSerializer(author).data
        return rep