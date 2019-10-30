from django.shortcuts import render, redirect
from .forms import LineForm, StationForm, ContactForm
from .models import Line, Station
from django.core import serializers
from django.contrib import messages
from django.core.exceptions import ValidationError


# Create your views here.


def index(request):
    form = LineForm(request.POST or None)
    list_of_lines = Line.objects.all()

    if form.is_valid():
        # form.save()
        new_contact = form.save()
        print('------------------------------')
        print(new_contact.id)
        # return redirect('line:index_page')

    return render(request, 'line/index.html', {'form': form, 'lines': list_of_lines})


def details(request):
    list_of_station_data = Station.objects.all()
    list_of_line_data = Line.objects.all()
    station_json_data = serializers.serialize('json', list_of_station_data)
    line_json_data = serializers.serialize('json', list_of_line_data)
    return render(request, 'line/details.html', {'stations': station_json_data, 'lines': line_json_data})


def create(request, id):
    form1 = StationForm(request.POST or None)
    form2 = LineForm(request.POST or None)
    item = Line.objects.get(pk=id)
    if form1.is_valid():
        # obj = form1.save(commit=False)
        # obj.line = item
        form2.save()
        # return redirect('line:show_and_create')
        print(form1.cleaned_data.get('id'))
        print(form2)
    return render(request, 'line/create.html', {'form1': form1, 'item': item, 'form2': form2})


def createStation(request):
    form1 = ContactForm
    form2 = LineForm
    if request.method == 'POST':
        form1 = ContactForm(request.POST)
        form2 = LineForm(request.POST)
    return render(request, 'line/create-station.html', {'station_form': form1, 'line_form': form2})


def save_stations(request):
    form1 = LineForm(request.POST)
    form2 = StationForm(request.POST)
    print('-------------------------')
    if form1.is_valid() and form2.is_valid():
        object = form1.save()
        line_name = request.POST.getlist('name')
        line_number = request.POST.getlist('line_number')
        is_nigt_route = request.POST.getlist('night_route')
        lats = request.POST.getlist('lat')
        lngs = request.POST.getlist('lng')
        station_name = request.POST.getlist('station_name')
        for i in range(1, len(lats)):
            obj = Station(lat=lats[i], lng=lngs[i],
                          station_name=station_name[i], line=object)
            obj.save()
        # else:
        #     raise ValidationError(
        #         "Sorry, the email submitted is invalid. All emails have to be registered on this domain only.")
    # print(lats, lngs, station_name, is_nigt_route, line_number, line_name)
    else:
        form1 = LineForm(request.POST)
        form2 = StationForm(request.POST)
    print('-------------------------')
    messages.success(request, f'Srkomanijak')

    return redirect('line:index_page')


def delete(request, id):
    item = Line.objects.get(id=id)
    item.delete()

    return redirect('line:index_page')


def edit(request, id):
    item = Line.objects.get(id=id)
    form = LineForm(request.POST or None, instance=item)
    return render(request, 'line/update.html', {'item': item, 'form': form})


def edit_save(request, id):
    item = Line.objects.get(id=id)
    form = LineForm(request.POST or None)
    if form.is_valid():
        form.save()
    messages.success(request, 'Srkomanijak')

    return redirect('line:index_page')


def oneLineDetais(request, id):
    line_data = Line.objects.get(id=id)
    list_of_station_data = Station.objects.filter(line__id=id)
    count = Station.objects.filter(line__id=id).count()
    myarray = []
    for i in range(0, count):
        myarray.append(12)
    station_json_data = serializers.serialize('json', list_of_station_data)
    line_json_data = serializers.deserialize('json', line_data)
    return render(request, 'line/one-line-details.html', {'stations': station_json_data, 'lines': line_data, 'count': myarray, 'lstations': list_of_station_data})
