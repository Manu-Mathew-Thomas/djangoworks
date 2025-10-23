from django.shortcuts import render
from app1.forms import  AdditionForm,SignupForm,CalorieForm


def addition(request):
    if request.method=="POST":
        #creating form_instance using submitted data
        form_instance=AdditionForm(request.POST)
        #check whether the data is valid
        if form_instance.is_valid():
            data=form_instance.cleaned_data
            print(data)
            n1=data['num1']
            n2=data['num2']
            s=int(n1)+int(n2)
            context={'result':s,'form':form_instance}

        return render(request,'addition.html',context)

    if (request.method == "GET"):
        form_instance=AdditionForm
        context={'form':form_instance}
        return render(request,'addition.html',context)


def signup(request):
    # success = False
    if request.method=="POST":
        print(request.POST)
        form_instance=SignupForm(request.POST)
        if form_instance.is_valid():
            success = True
            data=form_instance.cleaned_data
            print(data)
            n1 = data['username']
            n2 = data['password']
            n3 = data['place']
            n4 = data['gender']
            n5 = data['role']
            n6 = data['email']
            return render(request,'signup.html',{"form":form_instance,"success":success})

    if(request.method=="GET"):
        form_instance=SignupForm()
        context={'form':form_instance}
        return render(request,'signup.html',context)



def calorie(request):
    if(request.method=="POST"):
        form_instance=CalorieForm(request.POST)
        if form_instance.is_valid():
            data=form_instance.cleaned_data
            print(data)
            w=int(data['weight'])
            h=int(data['height'])
            a=int(data['age'])
            g=data['gender']
            al=float(data['activity_levels'])

            if g=="male":
                bmr=10*w+6.25*h-5*a+5
            else:
                bmr=10*w+6.25*h-5*a-161
            print(bmr)
            c=bmr*al
            context={'result':c,'form':form_instance}


            return render(request,'calorie.html',context)

    if(request.method=="GET"):

        form_instance=CalorieForm()
        context={'form':form_instance}
        return render(request,'calorie.html',context)


