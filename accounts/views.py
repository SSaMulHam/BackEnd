from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *


@login_required
@api_view(('GET', 'POST', 'PATCH'))
# Create your views here.
def profile(request, user_pk):
    if request.method == 'POST':
        pass

    else:
        profile = Profile.objects.get(id=user_pk)
        serializer = ProfileSerializer(profile)
        
        return JsonResponse(serializer.data)