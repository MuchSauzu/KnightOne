
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from django.shortcuts import render
from Dashboard.views import produk

def cobax (request):
    return HttpResponse('selamat datang')

def cobay (request):
    titelnya="Home"
    konteks = {
        'titel':titelnya,
    }
    return render(request, 'index.html',konteks)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', cobay),
    path('produk/', produk),
]
