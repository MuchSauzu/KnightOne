from django.shortcuts import render

# Create your views here.

def produk(request):
    titelnya="produk"
    konteks = {
        'titel':titelnya,
    }
    return render (request,'produk.html',konteks)