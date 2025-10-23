from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# def First(request):
#     return HttpResponse("First Page")
# def Second(request):
#     return HttpResponse("Second Page")
def first(request):
    context={'name':'arun','age':23}
    return render(request,'first.html')
def second(request):
    return render(request,'second.html')
