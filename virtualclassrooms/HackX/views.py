from django.shortcuts import render

# Create your views here.


def register(request):
    return render(request,'register.html')


def videocall(request):
    return render(request, 'videocall.html')