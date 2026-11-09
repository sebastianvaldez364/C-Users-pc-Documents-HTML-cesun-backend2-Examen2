from django.shortcuts import render, redirect
from .models import Auto
from .forms import AutoForm


# Vista para mostrar los autos registrados
def lista_autos(request):

    autos = Auto.objects.all()

    return render(request, 'autos/lista_autos.html', {
        'autos': autos
    })


# Vista para agregar nuevos autos
def agregar_auto(request):

    if request.method == 'POST':

        form = AutoForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('lista_autos')

    else:
        form = AutoForm()

    return render(request, 'autos/agregar_auto.html', {
        'form': form
    })