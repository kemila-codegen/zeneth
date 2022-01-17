from django.shortcuts import render
from .models import *

# Create your views here.


def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def our_collection(request):
    
    villas = villa.objects.all()
    read_more = readMore.objects.all()
    image_gallery_id = imageGallery.objects.all()

    return render(request, "our_collection.html", {'villas': villas, 'read_more': read_more, 'image_gallery_id': image_gallery_id})
    

def partner_with_us(request):
    return render(request, "partner_with_us.html")
