from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'accounts/home.html')


@login_required(login_url='/accounts/login')
def check_auth(request):
    return render(request, 'accounts/check.html')

