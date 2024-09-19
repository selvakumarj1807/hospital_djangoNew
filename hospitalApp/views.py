from django.shortcuts import render

from hospitalApp.models import Doctor

# Create your views here.
def index(request):
    doctors = Doctor.objects.filter(status=0)
    return render(request,"index.html", {'doctors': doctors})