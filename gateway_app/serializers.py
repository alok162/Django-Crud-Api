from rest_framework import serializers
# from myapp.models import Users
from gateway_app.models import Gateway
from gateway_app.models import Route_Map

from rest_framework import status



class GatewayPostSerializer(serializers.ModelSerializer):
		class Meta:
			model = Gateway
			fields = ['gateway_name', 'ip_addresses']


class GatewayGetSerializer(serializers.ModelSerializer):
		class Meta:
			model = Gateway
			fields = ['gateway_name', 'ip_addresses']


class RouteMappingPostSerializer(serializers.Serializer):
	gateway_id = serializers.IntegerField()
	prefix = serializers.CharField(max_length=200)
	def create(self, validated_data):
		return Route_Map.objects.create(**validated_data)


class RouteMappingGetSerializer(serializers.ModelSerializer):
    #model serializer inbuilt method with create() and update()
		class Meta:
			model = Route_Map
			fields = ['prefix', 'gateway_id']


class YourSerializer(serializers.Serializer):
   """Your data serializer, define your fields here."""
   gateway_name = serializers.CharField(max_length=200)


class GatewayPatchSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Gateway
        fields = ('gateway_name', 'ip_addresses')
