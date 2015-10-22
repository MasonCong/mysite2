from django.shortcuts import render
from django.http import HttpResponse
from event.models import Picture
from django.template import RequestContext, loader
import json
# Create your views here.
from django.http import JsonResponse

def index(request):
	picture_list=Picture.objects.order_by('-title_text')
	template=loader.get_template('event/index.html')
    	context = RequestContext(request, {'picture_list': picture_list,})
    	return HttpResponse(template.render(context))

def detail(request,picture_id):
	q=Picture.objects.get(pk=picture_id)
	res={}
	res["Title"]=q.title_text
	res["Description"]=q.description
	res["Image"]=q.picture_url
	#res=json.dumps(res)
	res=[res]
	return JsonResponse(res,safe=False)
