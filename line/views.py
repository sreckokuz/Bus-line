from django.shortcuts import render, redirect
from .forms import LineForm, StationForm, AdditionalForm
from .models import Line, Station
from django.core import serializers
from django.contrib import messages
from django.core.exceptions import ValidationError


# show index page with list of bus lines
def index(request):
    list_of_lines = Line.objects.all()
    return render(request, 'line/index.html', {'lines': list_of_lines})


# show all routes with station markers
def details(request):
    list_of_station_data = Station.objects.all()
    list_of_line_data = Line.objects.all()
    station_json_data = serializers.serialize('json', list_of_station_data)
    line_json_data = serializers.serialize('json', list_of_line_data)
    return render(request, 'line/details.html', {'stations': station_json_data, 'lines': line_json_data})


# create form for bus line, and multiple forms for stations
def createLineAndStations(request):
    form1 = AdditionalForm
    form2 = LineForm
    if request.method == 'POST':
        form1 = AdditionalForm(request.POST)
        form2 = LineForm(request.POST)
    return render(request, 'line/create-station.html', {'station_form': form1, 'line_form': form2})


# save all forms input
def save_stations(request):
    form1 = LineForm(request.POST)
    form2 = StationForm(request.POST)
    if form1.is_valid() and form2.is_valid():
        object = form1.save()
        lats = request.POST.getlist('lat')
        lngs = request.POST.getlist('lng')
        station_name = request.POST.getlist('station_name')
        for i in range(0, len(lats)):
            obj = Station(lat=lats[i], lng=lngs[i],
                          station_name=station_name[i], line=object)
            obj.save()
        # else:
        #     raise ValidationError(
        #         "Sorry, the email submitted is invalid. All emails have to be registered on this domain only.")
    # print(lats, lngs, station_name, is_nigt_route, line_number, line_name)
    return redirect('line:index_page')


# delete bus lines
def delete(request, id):
    item = Line.objects.get(id=id)
    item.delete()
    return redirect('line:index_page')


# edit bus line
def edit(request, id):
    item = Line.objects.get(id=id)
    form = LineForm(request.POST or None, instance=item)
    return render(request, 'line/update.html', {'item': item, 'form': form})


# save bus line. I had to work like this because form for input is tied to two models Line and Stations
def edit_save(request, id):
    item = Line.objects.get(id=id)
    form = LineForm(request.POST or None)
    if form.is_valid():
        form.save()
    messages.success(request, 'Edited')
    return redirect('line:index_page')


#
def oneLineDetais(request, id):
    line_data = Line.objects.get(id=id)
    list_of_station_data = Station.objects.filter(line__id=id)
    # ---------some improvisation that I wouldn't have to change
    count = Station.objects.filter(line__id=id).count()
    myarray = []
    for i in range(0, count):
        myarray.append(12)
    # ------
    station_json_data = serializers.serialize('json', list_of_station_data)
    line_json_data = serializers.deserialize('json', line_data)
    return render(request, 'line/one-line-details.html', {'stations': station_json_data, 'lines': line_data, 'count': myarray, 'lstations': list_of_station_data})
