from django.shortcuts import render
from django.template import RequestContext
from django.contrib.auth.models import User


def homepage_v(request):
    context = {'foo': 'bar'}
    return render(request, 'homepage.html', context)

def contact_v(request):
    context = {'foo': 'bar'}
    return render(request, 'contact.html', context)

def profile_v(request):
    context = {'foo': 'bar'}
    return render(request, 'user_profile.html', context)