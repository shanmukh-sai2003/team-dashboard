from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import *
# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    
    members = TeamMembers.objects.all()
    return render(request, 'coreMembers/index.html', {
        "members": members
    })

def updateOperation(request, id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))

    members = TeamMembers.objects.all()
    member = TeamMembers.objects.get(id = id)
    if request.method == 'POST':
        name = request.POST['name']
        role = request.POST['role']
        email = request.POST['email']
        phone = request.POST['phone']

        if not (name and role and email and phone):
            return render(request, 'coreMembers/update.html', {
            "member": member,
            "members": members,
            "message": "you cannot make any feild empty"
        })

        member.name = name
        member.role = role
        member.email = email
        member.phone = phone
        member.save()
        return HttpResponseRedirect(reverse('home'))
    
    
    if member:
        return render(request, 'coreMembers/update.html', {
            "member": member,
            "members": members
        })
    
def deleteOperation(request, id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    
    if request.method == 'GET':
        member = TeamMembers.objects.get(id = id)
        if member:
            member.delete()
            return HttpResponseRedirect(reverse('home'))
    return HttpResponse('deletepage')

def add(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))

    members = TeamMembers.objects.all()
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        role = request.POST['role']
        phone = request.POST['phone']
        
        if not (name and email and role and phone):
            return render(request, 'coreMembers/add.html', {
                "name": name,
                "email": email,
                "role": role,
                "phone": phone,
                "message": "every feild is compulsory",
                "members": members
            })
        
        member = TeamMembers.objects.filter(email = email)
        if member:
            return render(request, 'coreMembers/add.html', {
                "name": name,
                "email": email,
                "role": role,
                "phone": phone,
                "message": "already a team member exists with this email",
                "members": members
            })
        
        newMember = TeamMembers.objects.create(name = name, role = role, email = email, phone = phone)
        return HttpResponseRedirect(reverse('home'))
    
    return render(request, 'coreMembers/add.html', {
        "members": members
    })


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is None:
            return render(request, 'coreMembers/login.html', {
                "username": username,
                "message": "Invaild credentials!! please try again"
            })

        login(request, user)
        return HttpResponseRedirect(reverse('home'))


    return render(request, 'coreMembers/login.html')

def logout_view(request):
    logout(request)

    return HttpResponseRedirect(reverse('login'))


