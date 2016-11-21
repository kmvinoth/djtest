from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'org/home.html')


@login_required(login_url='/org/login')
def check_auth(request):
    return render(request, 'org/check.html')

