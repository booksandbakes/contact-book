from urllib import response
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import registerForm,loginForm,contactForm
from .models import user as userdata,contacts
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate,get_user_model,login,logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout



# Create your views here.
def home(request):
    form = loginForm(request.POST or None)
    if form.is_valid():
        if request.POST:
            username=request.POST['username']
            password=request.POST['password']
            user=authenticate(username=username,password=password)
            if user is not None:
                if user.is_active:
                    login(request,user)
                    res=add(request)
                    return HttpResponse('Loggined successfully!')

    context = {'form': form, }
    return render(request, "login.html", context)


def register(request):
    form = registerForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        user.set_password(request.POST['password'])
        user.save()
        new_data=userdata(name=request.POST['username'],email=request.POST['email'],password=request.POST['password'])
        new_data.save()          
        return redirect('/')

    context = {
        'form': form,
    }
    return render(request, "register.html", context)

from .serializer import ContactListDetailSerializer,UserListDetailSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser

@api_view(['GET'])
def add(request):
    data = contacts.objects.filter(user_id=request.user.email)
    serializer = ContactListDetailSerializer(data, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def register_api(request):
    #data = JSONParser().parse(request)
    print(request.POST['username'])
    data = JSONParser().parse(request)
    print(data,request.data)
    # serializer = UserListDetailSerializer(data)
    # if serializer.is_valid():
    #     serializer.save()
    #     return JsonResponse(serializer.data)
    # return JsonResponse(data={'failed to add'})

