from django.urls import path
from presents import views

urlpatterns = [
    # 선물 리스트 조회
    path('post/', views.PresentListAPIView.as_view(), name='post_list'),
    # 선물 상세 조회
    path('post/<int:pk>/', views.PresentRetrieveAPIView.as_view(), name='post_detail'),
    # 댓글 생성
    path('comment/', views.CommentCreateAPIView.as_view(), name='comment_create'),
    # 선물 좋아요 생성
    path('post/<int:pk>/like/', views.PresentLikeCreateAPIView.as_view(), name='post-like'),
    # 댓글 좋아요 생성
    path('comment/<int:pk>/like/', views.CommentLikeCreateAPIView.as_view(), name='comment-like'),
]
