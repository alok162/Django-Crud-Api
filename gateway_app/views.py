# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import json
from rest_framework.renderers import JSONRenderer

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import HttpResponse
from rest_framework import status
from gateway_app.models import Gateway
from gateway_app.models import Route_Map
from rest_framework import generics
from rest_framework.parsers import JSONParser
from django.http import Http404

from gateway_app.serializers import GatewayPostSerializer 
from gateway_app.serializers import GatewayGetSerializer
from gateway_app.serializers import RouteMappingPostSerializer 
from gateway_app.serializers import RouteMappingGetSerializer
from gateway_app.serializers import YourSerializer
from gateway_app.serializers import GatewayPatchSerilizer



class Gateway_Post(generics.ListCreateAPIView):
	queryset = Gateway.objects.all()
   	serializer_class = GatewayPostSerializer


class Gateway_Detail(generics.RetrieveUpdateAPIView):
	queryset = Gateway.objects.all()
   	serializer_class = GatewayGetSerializer


class GetPrefix(APIView):
    def get(self, request,pk, format=None):
		prefixdict = {}
		templist = []
		temp = Route_Map.objects.values()
		outstr=''
		for i in temp:
			prefixdict[i['prefix']]=i['gateway_id']
		for i in str(pk):
			outstr+=i
			if outstr in prefixdict:
				templist.append(outstr)
		print templist
		gateway_name = ''
		query = Route_Map.objects.all().select_related('gateway').filter(gateway=prefixdict[templist[len(templist)-1]])
		for i in query:
			gateway_name = i.gateway.gateway_name
		yourdata= [{"gateway_name": gateway_name}]
		results = YourSerializer(yourdata, many=True).data
		return Response(results)
		
		
class Route_Mapping(APIView):
    def post(self, request, format=None):
		data1 = JSONParser().parse(request)
		actual_data = {}
		actual_data['prefix'] = data1['prefix']
		actual_data['gateway_id'] = Gateway.objects.filter(gateway_name=data1['gateway_name']).values()[0]['id']
		serializer = RouteMappingPostSerializer(data=actual_data)
		print serializer
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Route_Mapping_Detail(APIView):
    def get(self, request,pk, format=None):
        obj = Route_Map.objects.all().select_related('gateway')
        serializer = RouteMappingGetSerializer(obj, many=True)
        resdata = {}
        resdata['prefix']=serializer.data[0]['prefix']
        for i in obj:
			resdata['gateway_name']=i.gateway.gateway_name
        return Response(resdata)
   	

class Gateway_Update(APIView):
    def get_object(self, pk):
        return Gateway.objects.get(pk=pk)

    def patch(self, request, pk):
        testmodel = self.get_object(pk)
        serializer = GatewayPatchSerilizer(testmodel, data=request.data, partial=True) # set partial=True to update a data partially
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(code=400, data="wrong parameters", status=status.HTTP_400_BAD_REQUEST)


class Gateway_Delete(APIView):
	def get_object(self, pk):
		try:
			return Gateway.objects.get(pk=pk)
		except Gateway.DoesNotExist:
			raise Http404
	def delete(self, request, pk, format=None):
		rout_map_obj = Route_Map.objects.get(gateway=pk)
		rout_map_obj.delete()
		Gateway.objects.get(pk=pk).delete()
		return Response(status=status.HTTP_204_NO_CONTENT)




