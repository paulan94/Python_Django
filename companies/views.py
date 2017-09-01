# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Stock
from .serializers import StockSerializer

from django.http import Http404

#stocks/
class StockList(APIView):

    def get(self, request):
        #return all the stocks that we have. everything in our db get is for reading information
        stocks = Stock.objects.all()
        serializer = StockSerializer(stocks, many=True) #specify there are many of them
        return Response(serializer.data)

    def post(self):
        #create new stock, post is for submitting forms
        pass

# Create your views here.









