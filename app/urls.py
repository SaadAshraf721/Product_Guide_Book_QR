from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView
from django.views.static import serve


urlpatterns = [
    path('', register),
    path('dash/',dash),
    path('login/',login),
    path('addproduct/',productcreate.as_view()),
    path('<pk>/edit/',editproduct.as_view()),
    path('<pk>/editlng/',editlang.as_view()),
    path('lang/',langv),
    path('lgas/',langadd.as_view()),
    path('langadd/',lang_ass),
    path('<pk>/deletelng/',deletelang.as_view()),
    path('<pk>/editass/',editlangass.as_view()),
    path('<pk>/deleteprod/',deleteprod.as_view()),
path('<pk>/deletelngass/',deletelngass.as_view()),
    path('logout/',logout),
    path('search/',search),
    path('detail/',detail),


]
