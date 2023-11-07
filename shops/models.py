from django.db import models
from django.conf import settings

# Create your models here.
class Shop(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='shops')
    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='like_shops'
    ) 
    
    # fields
    place = models.TextField()
    # 오프라인 관련 필드 삭제 ?
    is_online = models.BooleanField() # 1: 온라인, 0: 오프라인
    openhour = models.TextField()
    tel = models.CharField(max_length=255)
    score = models.IntegerField(null=True, default=0)

    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='like_shop'
    )
    dislike_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='dislike_shop'
    )
    

    

# 선물 하나 당 댓글 여러개
# 선물과 댓글은 1:N 관계
class ShopComment(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='shops')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='like_shop_comments'
    )
    
    # fields
    content = models.TextField()
    score = models.IntegerField()