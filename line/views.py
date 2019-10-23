from django.shortcuts import render, redirect
from .forms import LineForm
from .models import Line, Station

# Create your views here.


def index(request):
    form = LineForm(request.POST or None)
    list_of_lines = Line.objects.all()

    if form.is_valid():
        form.save()
        return redirect('line:index_page')

    return render(request, 'line/index.html', {'form': form, 'lines': list_of_lines})


def details(request):
    list_of_data = Station.objects.all()
    return render(request, 'line/details.html', {'items': list_of_data})
