from django.shortcuts import render
from django.http import HttpResponse
from event.models import Picture
import json
# Create your views here.
from django.http import JsonResponse

def index(request):
	return HttpResponse("Hello,world.")

def detail(request,picture_id):
	q=Picture.objects.get(pk=picture_id)
	res={}
	res["Title"]=q.title_text
	res["Description"]=q.description
	res["Image"]=q.picture_url
	return JsonResponse(res)
