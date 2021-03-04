from rest_framework import serializers
from .models import *

class TaskSerializer(serializers.ModelSerializer):
	class Meta:
		model = Task
		fields = '__all__'

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
	orderItems = serializers.SerializerMethodField(read_only=True)
	class Meta:
        model = Order
        fields = '__all__'