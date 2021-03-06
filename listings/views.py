from django.shortcuts import render, get_object_or_404
from .models import Listing
from realtors.models import Realtor
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from listings.choices import bedroom_choices, city_choices, price_choices
# Create your views here.

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(listings, 2)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {
        'listings': paged_listings
    }
    return render(request, 'listings/listings.html', context)

def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)
    return render(request, 'listings/listing.html', {'listing': listing, 'mvp_realtors': mvp_realtors})

def search(request):
    queryset_list = Listing.objects.order_by('-list_date')

    #keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)
    #city
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)

    #bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)
    #price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)

    context = {
        'city_choices' : city_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices' : price_choices,
        'listings': queryset_list,
        'values' : request.GET
    }
    return render(request, 'listings/search.html', context)