from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.views.decorators.csrf import csrf_protect
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.forms import ModelForm
from auto_partner.serializers import AutoSerializer
from auto_partner.models import Auto, Partner, AutoPartnerRelation

def base(request):
    return render(request, 'base.html')

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('auto_partner:base')
            else:
                messages.error(request, 'Invalid username or password')
        else:
            messages.error(request, 'Invalid username or password')
    form = AuthenticationForm()
    return render(request, 'auto_partner/login.html', {'form': form})

def logout_request(request):
    logout(request)
    messages.info(request, 'Logged out successfully!')
    return redirect('auto_partner:base')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "You have successfully registered!")
            return redirect('auto_partner:base')
        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])
    form = UserCreationForm
    return render(request,
                'auto_partner/register.html',
                context={"form": form})

def get_auto(request, auto_id):
    if request.method == 'GET':
        try:
            auto = Auto.objects.get(id=auto_id)
            print(auto)
            response = serializers.serialize('json', [auto])
        except Exception as e:
            print(e)
            response = [{'Error': 'No auto with that id'}]

    return HttpResponse(response, content_type='text/json')

@csrf_exempt
@api_view(['GET', 'POST'])
def create_auto(request):
    if request.method == 'POST':
        try:
            serializer = AutoSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
        except Exception as e:
            print(e)
            serializer = [{}]
    return Response(serializer.data, content_type='application/json')