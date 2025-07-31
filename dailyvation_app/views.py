from django.http import HttpResponse
from django.shortcuts import render
from dailyvation_app.models import MotivationalPost


def home(request):
    return HttpResponse("Welcome to Dailyvation!")


def dashboard(request):
    posts = MotivationalPost.objects.all()
    return render(request, 'dashboard.html', {"posts": posts})