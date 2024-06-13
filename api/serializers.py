#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 22:52:51 2024

@author: dangkhoa
"""
from rest_framework import serializers
from .models import ProductPortfolio,Profile,Content
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','password')
        extra_kwargs = {'password': {'write_only':True,'required': True}} #yêu c      
    def create(self,validated_data):
        user = User.objects.create_user(**validated_data)
        token = Token.objects.create(user = user)
        return token.key
    def update(self, instance, validated_data):
        # Implement logic to update an existing Model instance
        instance.user = validated_data.get('user', instance.user)
        # Update other fields as needed
        instance.save()
        return instance
    
class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)  # Or use other User field options
    class Meta:
        model = Profile
        fields = '__all__'  # Include all fields, or specify the desired fields

    def create(self, validated_data):
        # Access the current user object (if needed)
        user = self.context.get('request').user

        # Create the Model instance with the current user
        instance = Profile.objects.create(user=user, **validated_data)
        return instance

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductPortfolio
        fields = '__all__'

class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = '__all__'
        
    