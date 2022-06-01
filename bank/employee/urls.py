from django.urls import path
from . import views

from .views import index, create, edit, update, delete,login,user_logout, Home

urlpatterns=[
   # url(r'^$', views.index, name='index'),

   path('index/',index),
   path('create/',create),
   path('edit/<str:name>/',edit),
   path('update/<str:name>/', update),
   path("delete/<str:name>/", delete),
   path('login/', login),
   path('logout/', user_logout),
   path('', Home),


]
