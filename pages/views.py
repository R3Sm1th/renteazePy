from django.shortcuts import render
from listings.models import Listing
from agents.models import Agent
from listings.choices import price_choices, bedroom_choices, postcode_choices
# from django.http import HttpResponse
# Create your views here.
def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    context = {
        'listings': listings,
        'price_choices': price_choices,
        'bedroom_choices': bedroom_choices,
        'postcode_choices': postcode_choices
    }
    return render(request, 'pages/index.html', context)

def about(request):
    agents = Agent.objects.order_by('-start_date')[:3]
    mvp = Agent.objects.all().filter(is_mvp=True)
    context = {
        'agents': agents,
        'mvp': mvp
    }
    return render(request, 'pages/about.html', context)
