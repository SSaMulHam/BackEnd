from django.urls import path, include
from . import views 


urlpatterns = [
    # 로그인
    # path('', include('allauth.urls')),
    path('', include('rest_auth.urls')),
    # 회원가입 
    path('registration/', include('rest_auth.registration.urls')),
    # 프로필
    path('profile/<int:user_pk>/', views.profile)
]
