from rest_framework import serializers
from .models import Present, PresentComment


class PresenListtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Present
        fields = '__all__'


class PresentRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Present
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PresentComment
        fields = '__all__'


class PresentLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Present
        fields = '__all__'

class CateTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Present
        fields = '__all__'