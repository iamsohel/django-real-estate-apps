from rest_framework import generics

from listings.models import Listing
from realtors.models import Realtor

from .serializers import ListingSerializer
from .serializers import RealtorSerializer

class ListingAPIView(generics.ListAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer

class RealtorAPIView(generics.ListAPIView):
    queryset = Realtor.objects.all()
    serializer_class = RealtorSerializer