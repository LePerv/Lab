from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from fleetdata.models import Race


def index(request):
    races = Race.objects.all()
    template = loader.get_template('fleetdata/index.html')
    context = {
        'race_list': races,
    }
    return HttpResponse(template.render(context, request))