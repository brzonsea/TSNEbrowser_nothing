"""TSNEbrowser URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static

'''
from django.shortcuts import render

import json


def test(request):

	return_list = []
	image_list = models.ImageTable.objects.all()
	for image in image_list:
		image_data = # Read image
		return_list.append(image_data)





	a = []
	i1 = [0, 0, 255, 255, 255, 0, 0]
	i2 = [0, 0, 255, 255, 255, 255, 0]
	i3 = [0, 0, 255, 255, 255, 255, 255]
	a.append(i1)
	a.append(i2)
	a.append(i3)

	return render(request, "test.html", {"my_list": json.dumps(return_list)})
'''
urlpatterns = [
	#url(r'^test/$', test),
    url(r'^admin/', admin.site.urls),
    url(r'', include('browser.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
