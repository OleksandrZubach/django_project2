from django.shortcuts import render
from django.http import HttpResponse

def about(request):
    return render(request, 'multipage_app/about.html')

def main(request):
    return render(request, 'multipage_app/main.html')

def base(request):
    return render(request, 'multipage_app/base.html')