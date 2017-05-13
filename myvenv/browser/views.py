from django.shortcuts import render
from .models import Screenshot
#from .forms import PostForm


'''
list of all screenshots to be displayed!!
'''
def media_list (request):
	medias = Screenshot.objects.all()
	return render(request, 'browser/draw_map.html', {'medias': medias})



def media_one(request,path):
	media = Screenshot.objects.filter(name=path)
	return render(request, 'browser/draw_map.html', {'media': media})