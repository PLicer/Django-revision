from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def home(request):

    peoples = [
        {'name':'Hriitk', 'age':23},
        {'name':'Hritik2', 'age':24},
        {'name':'Hriitk3', 'age':25},
        {'name':'Hriitk4', 'age':26},
    ]

    return render(request,"index.html",context={'peoples':peoples})

def success_page(request):
    return HttpResponse("Hey this is a success page")
