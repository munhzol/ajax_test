from django.shortcuts import render,HttpResponse

# Create your views here.


def index(req):
    return render(req, 'index.html')


def check_req(req, title):
    return HttpResponse(f'this is a message from server, client sent to me {title}')