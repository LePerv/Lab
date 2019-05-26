from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from fleetdata.models import Race
from fleetdata.models import Pilot
from fleetdata.models import Starship
from fleetdata.models import Station
from fleetdata.models import Fleet


def index(request):
    template = loader.get_template('fleetdata/index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def race(request):
    races = Race.objects.all()
    template = loader.get_template('fleetdata/race.html')
    context = {
        'race_list': races,
    }
    return HttpResponse(template.render(context, request))

def pilot(request):
    pilots = Pilot.objects.all()
    template = loader.get_template('fleetdata/pilot.html')
    context = {
        'pilot_list': pilots,
    }
    return HttpResponse(template.render(context, request))
    
def starship(request):
    starships = Starship.objects.all()
    template = loader.get_template('fleetdata/starship.html')
    context = {
        'starship_list': starships,
    }
    return HttpResponse(template.render(context, request))
    
def station(request):
    stations = Station.objects.all()
    template = loader.get_template('fleetdata/station.html')
    context = {
        'station_list': stations,
    }
    return HttpResponse(template.render(context, request))

def fleet(request):
    fleets = Fleet.objects.all()
    template = loader.get_template('fleetdata/fleet.html')
    context = {
        'fleet_list': fleets,
    }
    return HttpResponse(template.render(context, request))

