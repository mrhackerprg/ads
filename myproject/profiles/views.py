from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request , "profiles/index.red.html")

def yellow(request):
    return render(request , 'profiles/index.yellow.html')

def blue(request):
    return render(request , 'profiles/index.blue.html')

def gothic(request):
    return render(request , 'profiles/index.gothic.html')

def green(request):
    return render(request , 'profiles/index.green.html')

def android(request):
    return render(request , 'profiles/index.android_green.html')

def red(request):
    return render(request , "profiles/index.red.html")