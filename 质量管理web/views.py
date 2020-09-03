import random
import json
import os

from django.shortcuts import render ,redirect
from django.http import JsonResponse
from django.views.decorators import csrf
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, StreamingHttpResponse
from django.conf import settings
from django.views.decorators.csrf import requires_csrf_token


def roots(request):
    return HttpResponse("这是首页,首页无它")


def page_not_found(request, exception=404):
    return render(request,'404.html')


def permission_denied(request, exception=403):
    return render(request,'403.html')


def page_error(request, exception=500):
    return render(request,'500.html')
