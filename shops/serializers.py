from rest_framework import serializers
from shops.models import Shop, ShopComment

class ShopListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = "__all__"

class ShopSerializerDetail(serializers.ModelSerializer):
        class Meta:
            model = Shop
            fields = "__all__"

class ShopCommentSerializer(serializers.ModelSerializer):
        class Meta:
            model = ShopComment
            fields = "__all__"