from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def testview(request):
    return HttpResponse("<h1 style='font-family:sans-serif;text-align:center;margin-top:23%;'>Working, live at heroku!</h1>")