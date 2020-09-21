from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name='index'),
    path("menu.html", views.menu, name='menu'),
    path("footer.html", views.footer, name='footer'),
    path("poezia.html", views.poezia, name='poezia'),
    path("proza.html", views.proza, name='proza'),
    path("tregimedhenovela.html", views.tregimedhenovela, name='tregimedhenovela'),
    path("romane.html", views.romane, name='romane'),
    path("dramatizimi.html", views.dramatizimi, name='dramatizimi'),
    path("dramatizimtregime.html", views.dramatizimtregime, name='dramatizimtregime'),
    path("dramatizimfilmavizatimore.html", views.dramatizimfilmavizatimore, name='dramatizimfilmavizatimore'),
    path("dramatizimedrama.html", views.dramatizimedrama, name='dramatizimedrama'),
    path("krijimet.html", views.krijimet, name='krijimet'),
    path("krijimetlirimi.html", views.krijimetlirimi, name='krijimetlirimi')
]