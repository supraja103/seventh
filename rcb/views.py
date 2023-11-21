from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def virat(request):
    return render(request,'kohli.html')
def siraj(request):
    return HttpResponse('mohammad siraj')