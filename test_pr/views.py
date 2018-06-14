import datetime

from django.http import HttpResponse
from django.shortcuts import render, render_to_response


# Create your views here.
from test_pr import models
from test_pr.models import Student


def sayHello(request):
    s = 'Hello World!'
    current_time = datetime.datetime.now()
    html = '<html><head></head><body><h1> %s </h1><p> %s </p></body></html>' % (s, current_time)
    return HttpResponse(html)

def showStudents(request):
    user_list = Student.objects.select_all()
    # list = [{id: 1, 'name': 'Jack'}, {id: 2, 'name': 'Rose'}]
    return render_to_response('student.html',{'students': user_list})
