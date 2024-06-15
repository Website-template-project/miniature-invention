#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 22:40:23 2024

@author: dangkhoa
"""

from django.urls import path,include
from rest_framework import routers
from .views import get_users,get_product_portfolio,change_product,lang,create_user,UserDetailView

router = routers.DefaultRouter()
#router.register("user/", UserViewSet) #register user oop way

urlpatterns = [
    path("",include(router.urls)),
    path("all_users/",get_users),
    path("products/",get_product_portfolio),
    path("change_product/",change_product),
    path("lang/",lang), 
    path("register/",create_user), #register user functional way
    path("get_info/",UserDetailView.as_view())
]