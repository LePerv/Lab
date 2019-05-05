from django.db import models


class Race(models.Model):
    name = models.CharField(max_length=200)

class Pilot(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    rank = models.CharField(max_length=200)
    age = models.IntegerField(default=-1)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)

class Starship(models.Model):
    name = models.CharField(max_length=200)
    pilot = models.ForeignKey(Pilot, on_delete=models.CASCADE)
    weaponry = models.CharField(max_length=200)
    payload = models.IntegerField(default=0)

class Station(models.Model):
    name = models.CharField(max_length=200)
    coordinates = models.CharField(max_length=200)
    hangar_size = models.IntegerField(default=0)
    is_military = models.BooleanField(default=False)
    director = models.ForeignKey(Pilot, on_delete=models.CASCADE)
    attributed_starships = models.ManyToManyField(Starship, through='StarshipAttribution')

class Fleet(models.Model):
    name = models.CharField(max_length=200)
    chief = models.ForeignKey(Pilot, on_delete=models.CASCADE)
    stations = models.ManyToManyField(Station, through='FleetAttribution')
    main_race = models.ForeignKey(Race, on_delete=models.CASCADE)

class StarshipAttribution(models.Model):
    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    starship = models.ForeignKey(Starship, on_delete=models.CASCADE)

class FleetAttribution(models.Model):
    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    fleet = models.ForeignKey(Fleet, on_delete=models.CASCADE)
