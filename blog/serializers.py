from blog.models import Post
from rest_framework import serializers
from django.contrib.auth.models import User
from django.utils import timezone

class PostSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Post
        fields = ('author', 'title', 'text', 'created_date', 'published_date', 'image')

    def create(self, validated_data):
        # API로 포스트 생성 시 published_date가 없으면 현재 시간으로 설정
        if 'published_date' not in validated_data or validated_data['published_date'] is None:
            validated_data['published_date'] = timezone.now()
        return super().create(validated_data)

