from django.contrib import admin
from django.urls import path
# from info.views import get_Family,get_Animal,get_Animals_all
import views
urlpatterns = [    
    path('family/<int:person_id',views.get_Family),
    path('animal/<int:person_id',views.get_Animal),
    path('family/<int:person_id',views.get_Animals_all),
]