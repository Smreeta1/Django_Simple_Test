from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Item

def index(request):
    items = Item.objects.all()
    return HttpResponse(f"Number of items: {items.count()}")
