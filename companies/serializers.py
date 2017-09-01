from rest_framework import serializers
from .models import Stock

class StockSerializer(serializers.ModelSerializer):

    class Meta:
        model = Stock
        #specify what attr to return
        # field = ('ticker', 'volume')
        #or return all
        fields = '__all__'