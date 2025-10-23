from django.shortcuts import render

def addition(request):
    if(request.method=="POST"):
        print(request.POST)
        n1=int(request.POST['n1'])
        n2=int(request.POST['n2'])
        s=n1+n2
        context={'result':s}
        return render(request,'addition.html',context)

    if(request.method=="GET"):
        return render(request,'addition.html')