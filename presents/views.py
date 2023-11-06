from requests import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from .models import Present, PresentComment
from.serializers import *

# 선물 리스트 조회
class PresentListAPIView(ListAPIView):
    qurtyset = Present.objects.all()
    serializer_class = PresenListtSerializer

# 선물 상세 조회
class PresentRetrieveAPIView(RetrieveAPIView):
    queryset = Present.objects.all()
    serializer_class = PresentRetrieveSerializer

# 댓글 생성
class CommentCreateAPIView(CreateAPIView):
    queryset = PresentComment.objects.all()
    serializer_class = CommentSerializer

# 선물 좋아요 생성
class PresentLikeCreateAPIView(GenericAPIView):
    queryset = Present.objects.all()

    def get(self, args, **kwargs):
        instance = self.get_object()
        instance.like += 1
        instance.save()

        return Response(instance.like)
    
# 댓글 좋아요 생성
class CommentLikeCreateAPIView(GenericAPIView):
    queryset = PresentComment.objects.all()

    def get(self, args, **kwargs):
        instance = self.get_object()
        instance.like += 1
        instance.save()

        return Response(instance.like)