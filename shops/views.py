
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, GenericAPIView

from shops.models import Shop, ShopComment
from shops.serializers import ShopCommentSerializer, ShopListSerializer, ShopSerializerDetail

# Create your views here.

class ShopListAPIView(ListAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopListSerializer


class ShopRetrieveAPIView(RetrieveAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializerDetail


class ShopCommentCreateAPIView(CreateAPIView):
    queryset = ShopComment.objects.all()
    serializer_class = ShopCommentSerializer


class ShopLikeAPIView(GenericAPIView):
    queryset = Shop.objects.all()

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.like += 1
        instance.save()
        return Response(instance.like)

class ShopDislikeAPIView(GenericAPIView):
    queryset = Shop.objects.all()

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.dislike_users += 1
        instance.save()
        return Response(instance.dislike_users)


# class ShopCommentLikeAPIView(GenericAPIView):
#     queryset = ShopComment.objects.all()
#     serializer_class = ShopCommentSerializer


# class ShopCommentDislikeAPIView(GenericAPIView):
#     queryset = ShopComment.objects.all()
#     serializer_class = ShopCommentSerializer