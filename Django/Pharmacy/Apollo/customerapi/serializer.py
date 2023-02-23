from rest_framework import serializers
from customer.models import Medicine

class list_med_serial(serializers.ModelSerializer):
    class Meta:
        model = Medicine
        fields = ('id', 'med_name', 'med_price', 'disease')