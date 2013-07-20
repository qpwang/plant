# -*- coding:utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext


def login(request):
    data = {'username': 'wqq'}
    return render_to_response('auth/login.html', data,
            context_instance=RequestContext(request))

def logout(request):
    data = {'username': 'wqq'}
    return render_to_response('auth/logout.html', data,
            context_instance=RequestContext(request))

def signup(request):
    data = {'username': 'wqq'}
    return render_to_response('auth/signup.html', data,
            context_instance=RequestContext(request))
