from django.db import models

# Create your models here.


class Poezi(models.Model):

    video = models.TextField(max_length=200, name=None)
    lecture_name = models.CharField(max_length=200)
    name = models.CharField(max_length=100)
    names = models.CharField(max_length=100)
    desc = models.TextField(max_length=300, name=None)

    def __str__(self):
        return self.lecture_name


        # Proze
class Prozeperralla(models.Model):

    video = models.TextField(max_length=200, name=None)
    lecture_name = models.CharField(max_length=200)
    name = models.CharField(max_length=100)
    names = models.CharField(max_length=100)
    desc = models.TextField(max_length=300, name=None)

    def __str__(self):
        return self.lecture_name


class Tregimedhenovela(models.Model):
    
    video = models.TextField(max_length=200, name=None)
    lecture_name = models.CharField(max_length=200)
    name = models.CharField(max_length=100)
    names = models.CharField(max_length=100)
    desc = models.TextField(max_length=300, name=None)

    def __str__(self):
        return self.lecture_name

class Romane(models.Model):
    
    video = models.TextField(max_length=200, name=None)
    lecture_name = models.CharField(max_length=200)
    name = models.CharField(max_length=100)
    names = models.CharField(max_length=100)
    desc = models.TextField(max_length=300, name=None)

    def __str__(self):
        return self.lecture_name



            # DRAMATIZIM
class Dramatizimperralla(models.Model):

    video = models.TextField(max_length=200, name=None)
    lecture_name = models.CharField(max_length=200)
    name = models.CharField(max_length=100)
    names = models.CharField(max_length=100)
    desc = models.TextField(max_length=300, name=None)

    def __str__(self):
        return self.lecture_name


class Dramatizimtregime(models.Model):

    video = models.TextField(max_length=200, name=None)
    lecture_name = models.CharField(max_length=200)
    name = models.CharField(max_length=100)
    names = models.CharField(max_length=100)
    desc = models.TextField(max_length=300, name=None)

    def __str__(self):
        return self.lecture_name

class Dramatizimfilmavizatimore(models.Model):

    video = models.TextField(max_length=200, name=None)
    lecture_name = models.CharField(max_length=200)
    name = models.CharField(max_length=100)
    names = models.CharField(max_length=100)
    desc = models.TextField(max_length=300, name=None)

    def __str__(self):
        return self.lecture_name


class Dramatizimedrama(models.Model):

    video = models.TextField(max_length=200, name=None)
    lecture_name = models.CharField(max_length=200)
    name = models.CharField(max_length=100)
    names = models.CharField(max_length=100)
    desc = models.TextField(max_length=300, name=None)

    def __str__(self):
        return self.lecture_name

            # Classroom
class Krijimeabetare(models.Model):

    video = models.TextField(max_length=200, name=None)
    lecture_name = models.CharField(max_length=200)
    name = models.CharField(max_length=100)
    names = models.CharField(max_length=100)
    desc = models.TextField(max_length=300, name=None)

    def __str__(self):
        return self.lecture_name

class Krijimelirimi(models.Model):

    video = models.TextField(max_length=200, name=None)
    lecture_name = models.CharField(max_length=200)
    name = models.CharField(max_length=100)
    names = models.CharField(max_length=100)
    desc = models.TextField(max_length=300, name=None)

    def __str__(self):
        return self.lecture_name




