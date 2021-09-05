from django.urls import path
from . import views
from django.conf.urls import include
urlpatterns = [
    #path('', views.index, name='index'),
	path('/homepage', views.homepageView, name='homepage'),
    # path('', include('bootstrap4.urls')),
]