from urllib.request import Request
from django.shortcuts import render
from django.http import HttpRequest,JsonResponse

# Create your views here.
def index_view(request):
    return render(request,'template/index.html')    

def about_view(request):
    return render(request,'template/about.html')

def contact_view(request):
    return render(request,'template/contact.html')

def services_view(request):
    return render(request,'template/services.html')

    
