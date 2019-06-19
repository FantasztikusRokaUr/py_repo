# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from treasures import Treasures

# Create your views here.

def index(request):

	return render(request, 'index.html', {'treasures':treasures})
	
treasures = [
	Treasures('Gold Nugget', 500.0, 'gold', 'Basin, GE', 'https://online.kitco.com/products/Degussa10-g-Gold-Nugget-Pendant-3003L/enu-Degussa10-g-Gold-Nugget-Pendant-3003L-20000-2.jpg'),
	Treasures("Fool's Gold", 000.0, 'pyrite', 'Hill, NE', 'https://images-na.ssl-images-amazon.com/images/I/51itMQJozsL.jpg'),
	Treasures('Coffee Can', 20.0, 'tin', 'Shores, BA', 'https://media.tiffany.com/is/image/Tiffany/60559112_973825_ED?$EcomItemL$&id=5rlr51&fmt=jpg&fit=constrain,1&wid=697&hei=697')
	]