from django.shortcuts import render
from django.core import serializers

import json
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
