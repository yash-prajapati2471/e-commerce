from django.shortcuts import render
from store.models import product

def index(request):

    pro = product.objects.all()

    context = {
        'product':pro,
    }
    return render(request,'index.html',context)