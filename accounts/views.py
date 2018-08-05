
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout, login




def logout_view(request):

    logout(request)
    return HttpResponseRedirect(reverse('index'))

def login_view(request):
    login(request)
    return HttpResponseRedirect(reverse('index'))
