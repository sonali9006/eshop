from django.urls import path
from django.urls.conf import include
from Eshop_prac_prac3 import settings
from app.views.index import Index

urlpatterns = [
    path('',Index.as_view() , name='index'),
]
