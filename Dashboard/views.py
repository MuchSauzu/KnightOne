from django.shortcuts import render

# Create your views here.

def pricing(request):
    titelnya="pricing"
    konteks = {
        'titel':titelnya,
    }
    return render(request, 'pricing.html',konteks)