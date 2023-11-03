from django.db import models
from django.conf import settings

# Create your models here.
class Present(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='presents')
    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='like_presents'
    ) 
    
    # fields
    name = models.TextField()
    price = models.IntegerField()
    image = models.ImageField()
    
    

# 선물 하나 당 댓글 여러개
# 선물과 댓글은 1:N 관계
class PresentComment(models.Model):
    present = models.ForeignKey(Present, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='like_present_comments'
    )
    
    # fields
    content = models.TextField()
    score = models.IntegerField()