from django.http import HttpResponse
from django.shortcuts import render
from . models import Place
from . models import Team


# Create your views here.
def home(request):
    # obj = Place.objects.all()
    obj = Team.objects.all()

    # return render(request,"index.html", {'result':obj})
    return render(request, "index.html", {'result1': obj})








