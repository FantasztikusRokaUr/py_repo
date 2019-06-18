# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


# Create your views here.

def index(request):
	name = 'Gold Nugger'
	value = 1000.00
	context = {'treasure_name': name,
			   'treasure_value': value}

	return render(request, 'index.html', context)
	
