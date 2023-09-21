from django.shortcuts import render
from listings.models import Listing
from agents.models import Agent
# from django.http import HttpResponse
# Create your views here.
def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    context = {
        'listings': listings
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
