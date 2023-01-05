from rest_framework import serializers
from .models import Hotel
from adresses import seralizers
from adresses.models import Address
import ipdb

class HotelSerializer(serializers.ModelSerializer):
    address = seralizers.AddressSerializer()

    class Meta:
        model = Hotel
        fields = ["id", 'owner', 'address']
        read_only_fields = ['owner']

    def create(self, validated_data):
     address_dict =  validated_data.pop("address")
     address_obj = Address.objects.create(**address_dict)
     hotel_obj = Hotel.objects.create(**validated_data, address=address_obj)
     return hotel_obj
     
