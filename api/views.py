import json
from django.core import serializers
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from api.serialisers import QuestionSerializer
from .models import Question
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
# Create your views here.
def testview(request):
    return HttpResponse("<h1 style='font-family:sans-serif;text-align:center;margin-top:23%;'>Working, live at heroku!</h1>")

@api_view(["GET"])
@permission_classes((permissions.AllowAny,))
def question_api(request):
    qs = set(Question.objects.all())
    ser = QuestionSerializer(qs, many=True)
    return Response(ser.data)
    # return JsonResponse(qs_json, content_type='application/json', safe=False)