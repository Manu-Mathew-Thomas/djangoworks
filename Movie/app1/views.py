from django.shortcuts import render
from app1.models import Moviedetails

def movielist(request):
    if(request.method=="GET"):
        m=Moviedetails.objects.all()
        context={'movies':m}
        return render(request,'movielist.html',context)

from app1.forms import MovieForm
def addmovie(request):
    if(request.method=="POST"):
        form_instance=MovieForm(request.POST,request.FILES)
        if form_instance.is_valid():
            form_instance.save()
            return render(request,'addmovie.html')
    if(request.method=="GET"):
        form_instance=MovieForm()
        context={'form':form_instance}
        return render(request,'addmovie.html',context)