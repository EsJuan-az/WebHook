from django.shortcuts import render,redirect
from .forms import *
from main.models import *
import random
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

    return render(request,'main/gethooked.html',{
        'inGetHooked':True,
        'categorie':categorie,
        'pages':pages
    })

def categories(request):
    categories = list(Categorie.objects.all())
    random.shuffle(categories,random.random)
    return render(request,'main/categories.html',{
        'categories':categories,
        'inCategories':True
    })

def submitHooks(request):
    formulario = PageForm()
    if request.method == 'POST':
        formulario = PageForm(request.POST)
        if formulario.is_valid():
            dataform = formulario.cleaned_data
            print(dataform)
            page = Pages(
                name=dataform['name'],
                url=dataform['url'],
                categories = dataform['categorie']
            )
            page.save()
            return redirect('home')
    return render(request,'main/submitHooks.html',{
        'inHooks':True,
        'form':formulario,
    })