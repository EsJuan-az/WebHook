from django.shortcuts import render
from main.models import *
# Create your views here.
def homePage(request):
    return render(request,'main/homepage.html',{
        'inHome':True
    })

def getHooked(request,categorie="Randomly"):
    if categorie == "Randomly":
        pages = Pages.objects.all()
        categorie = Categorie.objects.get(name=categorie)
    else:
        try:
            categorie = Categorie.objects.get(name=categorie)
            pages = Pages.objects.filter(categories_id = categorie.id)
        except:
            categorie,pages = False,False
    return render(request,'main/getHooked.html',{
        'inGetHooked':True,
        'categorie':categorie,
        'pages':pages
    })

def categories(request):
    categories = Categorie.objects.all()
    return render(request,'main/categories.html',{
        'categories':categories,
        'inCategories':True
    })