from rest_framework import serializers

from listings.models import Listing
from realtors.models import Realtor 

class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing 
        # ('__all__')  for all fields
        # ['quote', 'author']
        #fields = ['quote', 'author']
        fields = ('__all__')

class RealtorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Realtor 
        # ('__all__')  for all fields
        # ['title']
        fields = ('__all__')