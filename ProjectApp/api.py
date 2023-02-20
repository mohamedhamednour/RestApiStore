from rest_framework import serializers
from .models import Product, OrderItem, Cart
from django.contrib.auth.models import User

#hide importn
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User()
        exclude = ['password', 'last_login', 'is_superuser', 'is_staff',
                   'date_joined', 'groups', 'user_permissions']


class Products(serializers.ModelSerializer):


    class Meta:
        model = Product
        fields = '__all__'


class order(serializers.ModelSerializer):


    order_user = UserSerializer()

    class Meta:
        model = OrderItem
        fields = '__all__'
        depth = 1


class cart(serializers.ModelSerializer):

    order_user = UserSerializer()

    class Meta:
        model = Cart
        fields = '__all__'
        depth = 1



