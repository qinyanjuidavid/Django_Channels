from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm

def Registration(request):
    if request.method=="POST":
        form=UserCreationForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/chat/login/')
    else:
        form=UserCreationForm()
    context={
    'form':form
    }
    return render(request,'accounts/registration.html',context)
