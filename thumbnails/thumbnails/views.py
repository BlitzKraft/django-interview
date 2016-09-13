from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.template.defaulttags import csrf_token
from django.shortcuts import render
from django import forms

def index(request):
    return HttpResponseRedirect('image_sizes')
