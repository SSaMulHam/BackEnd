from django.urls import path
from . import views

urlpatterns = [
    # 전체 리스트
    path('', views.ShopListAPIView.as_view(), name='shop-list'),

    # 상세 정보
    path('<int:pk>/', views.ShopRetrieveAPIView.as_view(), name='shop-detail'),

    # 댓글 작성
    path('shopcomment/', views.ShopCommentCreateAPIView.as_view(), name='shop-comment-list'),

    # shoplike
    path('<int:pk>/like/', views.ShopLikeAPIView.as_view(), name='shop-like'),

    # shopdislike
    path('<int:pk>/dislike/', views.ShopDislikeAPIView.as_view(), name='shop-dislike'),

    # # shopcommentlike
    # path('shopcomment/<int:pk>/like/', views.ShopCommentLikeAPIView.as_view(), name='shopcomment-like'),

    # # shopcommentsdislike
    # path('shopcomment/<int:pk>/dislike/', views.ShopCommentDislikeAPIView.as_view(), name='shopcomment-dislike'),


]
