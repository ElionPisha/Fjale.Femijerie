from django.shortcuts import render
from .models import Poezi, Prozeperralla, Tregimedhenovela, Romane, Dramatizimperralla, Dramatizimtregime, Dramatizimfilmavizatimore, Dramatizimedrama, Krijimeabetare, Krijimelirimi
def menu(request):
    return render(request, 'menu.html')

def footer(request):
    return render(request, 'footer.html')

def testimonials(request):
    return render(request, 'testimonials.html')


def index(request):
    return render(request, 'index.html')


            #Poezia
def poezia(request):
    videos = Poezi.objects.all()
    return render(request, 'poezia.html', {'videos': videos})


            #PROZA
def proza(request):
    videos = Prozeperralla.objects.all()
    return render(request, 'proza.html', {'videos': videos})


def tregimedhenovela(request):
    videos = Tregimedhenovela.objects.all()
    return render(request, 'tregimedhenovela.html', {'videos': videos})


def romane(request):
    videos = Romane.objects.all()
    return render(request, 'romane.html', {'videos': videos})

            # Dramatizim
def dramatizimi(request):
    videos = Dramatizimperralla.objects.all()
    return render(request, 'dramatizimi.html', {'videos': videos})

def dramatizimtregime(request):
    videos = Dramatizimtregime.objects.all()
    return render(request, 'dramatizimtregime.html', {'videos': videos})

def dramatizimfilmavizatimore(request):
    videos = Dramatizimfilmavizatimore.objects.all()
    return render(request, 'dramatizimfilmavizatimore.html', {'videos': videos})

def dramatizimedrama(request):
    videos = Dramatizimedrama.objects.all()
    return render(request, 'dramatizimedrama.html', {'videos': videos})


           #Krijime
def krijimet(request):
    videos = Krijimeabetare.objects.all()
    return render(request, 'krijimet.html', {'videos': videos}) 

def krijimetlirimi(request):
    videos = Krijimelirimi.objects.all()
    return render(request, 'krijimetlirimi.html', {'videos': videos})  





