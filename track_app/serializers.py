from rest_framework import serializers
from .models import Expense
from djoser.serializers import UserCreateSerializer



class ExpenseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Expense
        fields = ['id', 'categotry', 'description', 'amount']


class MyUserSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        fields = ['id', 'username', 'email', 'last_name', 'password']