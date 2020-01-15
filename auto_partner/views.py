from django.shortcuts import render

def login(request):
    return render(request, 'auto_partner/login.html')
