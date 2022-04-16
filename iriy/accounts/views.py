from django.shortcuts import render
from django.http import HttpResponse


def index(req):
    # return render(request=req, template_name='accounts/index.html')
    return HttpResponse("<h4>Somethink</h4>")


def reg(req):
    return render(request=req, template_name='accounts/index.html')


def profile_f(req):
    pass