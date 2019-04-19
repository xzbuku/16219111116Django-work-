
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from app1.models import Phone
from django.core.paginator import Paginator
# Create your views here.
def index(request,num):
    li=Phone.objects.all()[:100]
    pgs=Paginator(li,10)
    if(num>pgs.num_pages):
        return render(request, 'index.html', {"ls": pgs.page(pgs.num_pages)})
    if (num<=1):
        return render(request, 'index.html', {"ls": pgs.page(1)})
    return render(request, 'index.html',{"ls":pgs.page(num)})
def ss(request):
    return HttpResponseRedirect('index/1')
