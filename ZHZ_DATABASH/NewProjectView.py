from django.shortcuts import render,redirect
from django.http import HttpResponse
from. import models
from django.http import JsonResponse
# import  json
# from django.core import serializers

# -----------------------------page部分---
def New_project(request):
    """
    新项目，
    """
    return HttpResponse("新项目管理页面")


def New_project_json(request):
    """
    新项目的接口
    """
    NewProjectS = models.NewCompanyProject.objects.all().values()
    data = {}
    data["projects"] = list(NewProjectS)
    return JsonResponse(data, safe=False)


# -----------------------------api部分---