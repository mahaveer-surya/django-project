from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.

def studentView(response):
    students ={
            'id':1,
            'name':"mahaveer"
        }
    return JsonResponse(students)