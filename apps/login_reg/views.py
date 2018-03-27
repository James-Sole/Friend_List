# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect, reverse
from django.contrib import messages
from models import *
import bcrypt
def index(request):
	return render(request, "login_reg/index.html")
def login(request, methods = ['POST']):
    errors = User.objects.login_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request,error)
        return redirect('/')
    request.session['id']= User.objects.get(username = request.POST['username']).id
    request.session['status']= 'logged in'
    return redirect('/friends')

def register(request, methods = ['POST']):
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request,error)
        return redirect('/')
    password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
    User.objects.create(name = request.POST['name'], username = request.POST['username'], email = request.POST['email'], password = password, birth_date = request.POST['birth_date'])
    request.session['id']= User.objects.last().id
    request.session['status']= 'registered'
    return redirect('/friends')

def friends(request):
    if 'id' in request.session:
        context = {
            'username' : User.objects.get(id =request.session['id']).username,
            'my_friends': User.objects.filter(friends = request.session['id']),
			'other_people': User.objects.exclude(friends = request.session['id']),
        }
        return render(request, "login_reg/success.html", context)
    return redirect('/')

def userId(request, id):
    if 'id' in request.session:
        context = {
            'username' : User.objects.get(id = id).username,
            'name' : User.objects.get(id = id).name,
            'email' : User.objects.get(id = id).email,

        }
        return render(request, 'login_reg/user.html', context)
    return redirect('/')

def Add(request, id):
	#add relationship
	user = User.objects.get( id=request.session['id'])
	friend = User.objects.get(id = id)
	friend.friends.add(user)
	return redirect('/friends')

def Remove(request, id):
	pass
	#remove relationship
    #coundnt properly access the relationships table because i didnt know what it was named i oppedned my shell and tried all the names that seemed to match the named feild in my database

def logout(request):
    request.session.clear()
    return redirect('/')

# Create your views here.
