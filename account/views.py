from django.shortcuts import render
from .forms import RegisterForm
# Create your views here.

def Register(request):
    form = RegisterForm()

    context = {
        'form':form,
    }
    return render(request,'account/register.html',context)