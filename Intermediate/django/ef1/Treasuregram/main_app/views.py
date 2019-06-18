# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from treasures import Treasures

# Create your views here.

def index(request):

	return render(request, 'index.html', {'treasures':treasures})
	
treasures = [
	Treasures('Gold Nugget', 500.0, 'gold', 'Basin, GE'),
	Treasures("Fool's Gold", 000.0, 'pyrite', 'Hill, NE'),
	Treasures('Coffee Can', 20.0, 'tin', 'Shores, BA')
	]