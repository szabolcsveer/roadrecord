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
from auto_partner.serializers import AutoSerializer, PartnerSerializer
from auto_partner.models import Auto, Partner, AutoPartnerRelation
from django.contrib.auth.decorators import login_required

def base(request):
    return render(request, 'base.html')
@csrf_exempt
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

# AUTO REQUESTS

@login_required(login_url='/login')
def get_all_auto(request):
    if request.method == 'GET':
        all_autos = Auto.objects.all()
        print(all_autos)
        response = []
        for item in all_autos:
            obj = dict(driver = item.driver,)
            response.append(obj)
    return HttpResponse(response)

@login_required(login_url='/login')
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

@login_required(login_url='/login')
@csrf_exempt
@api_view(['GET', 'POST'])
def create_auto(request):
    if request.method == 'POST':
            serializer = AutoSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)         
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@login_required(login_url='/login')
@csrf_exempt
@api_view(['DELETE'])
def delete_auto(request, auto_id):
    auto = Auto.objects.get(id=auto_id)
    if auto is not None:
        if request.method == 'DELETE':
            return Response(status=status.HTTP_204_NO_CONTENT)

# PARTNER REQUESTS
# @login_required(login_url='/login')
def get_partner(request, partner_id):
    if request.method == 'GET':
        try:
            partner = Partner.objects.get(id=partner_id)
            print(partner)
            response = serializers.serialize('json', [partner])
        except Exception as e:
            print(e)
            response = [{'Error': 'No partner with that id'}]

    return HttpResponse(response, content_type='text/json')

# @login_required(login_url='/login')
@csrf_exempt
@api_view(['GET', 'POST'])
def create_partner(request):
    if request.method == 'POST':
            serializer = PartnerSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)         
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @login_required(login_url='/login')
@csrf_exempt
@api_view(['DELETE'])
def delete_partner(request, partner_id):
    partner = Partner.objects.get(id=partner_id)
    if request.method == 'DELETE':
        partner.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

# @csrf_exempt
# @api_view(['GET', 'POST'])
# def create_auto_partner_relation(request):
#     if request.method == 'POST':
