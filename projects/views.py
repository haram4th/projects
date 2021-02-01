from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse("안녕하세요. 황성민의 Portfolio 페이지에 오신 것을 환영합니다.")