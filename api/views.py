import json
from django.core import serializers
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Question
# Create your views here.
def testview(request):
    return HttpResponse("<h1 style='font-family:sans-serif;text-align:center;margin-top:23%;'>Working, live at heroku!</h1>")

def question_api(request):
    qs = Question.objects.all()
  
    qs_json = serializers.serialize('json', qs)
    return JsonResponse(qs_json, content_type='application/json', safe=False)