from rest_framework import serializers

from . models import *

# category serializer
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

# product serializer
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'       

# cart serializer
class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'

# cartProduct serializer
class CartProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartProduct
        fields = '__all__'

# Order serializer
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

# Check serializer
class CheckOutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        exclude = ['cart', 'subtotal', 'amount', 'ref', 'order_status', 'order_completed']


