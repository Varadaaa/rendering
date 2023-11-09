from django.shortcuts import render

# Create your views here.
def madhan(request):
    return render(request, 'madhan.html')

def bharathi(request):
    return render(request,'bharathi.html')

def ramani(request):
    return render(request, 'ramani.html')

def annu (request):
    return render(request, 'annu.html')

def sumi (request):
    return render(request, 'sumi.html')