from django.shortcuts import redirect, render

from hospitalApp.forms import AppointmentForm
from hospitalApp.models import Doctor

# Create your views here.
def index(request):
    doctors = Doctor.objects.filter(status=0)
    form = AppointmentForm()  # Instantiate the form
    return render(request,"index.html", {'doctors': doctors, 'form': form})

def addnew(request):
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = AppointmentForm()
    return render(request, "index.html", {'form': form})
