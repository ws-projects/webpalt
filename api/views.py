# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.views.decorators.csrf import csrf_exempt
 
@csrf_exempt
@api_view(http_method_names=['post'])        #只允许post
@permission_classes((permissions.AllowAny,))

def index(request):
  parameter = request.data
  id = parameter['data']
  if id == 1:
    data = 'There are three dogs'
  elif id == 2:
    data = 'There are two dogs'
  else:
    data = 'nothing'
  return Response({'data':data})