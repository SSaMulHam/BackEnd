from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.views import APIView


# 선물 리스트 조회
class PresentListAPIView(ListAPIView):
    pass

# 선물 상세 조회
class PresentRetrieveAPIView(RetrieveAPIView):
    pass

# 댓글 생성
class CommentCreateAPIView(CreateAPIView):
    pass

# 좋아요 생성
class PresentLikeCreateAPIView(serializers.ModelSerializer):
    pass  

# 카테고리
class CateTagAPIView(APIView):
    pass