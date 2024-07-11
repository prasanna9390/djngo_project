from django.urls import path
from accounts import views

urlpatterns = [
    path('',views.index),
    path('userreg/',views.userreg,name='userreg'),
   
    
]