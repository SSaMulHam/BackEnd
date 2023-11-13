from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Shop(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='shops')
    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='like_shops'
    ) 
    # fields
    place = models.TextField() # place : 브랜드 네임
    # openhour = models.TextField()
    tel = models.CharField(max_length=255)
    # validator활용하여 평점 0~5점만 줄 수 있도록 설정
    score = models.IntegerField(null=True, default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])



    

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
    score = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])