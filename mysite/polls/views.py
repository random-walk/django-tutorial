from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("print from polls/views.py index")

def detail(request, question_id):
    return HttpResponse('this is question id: %s' % question_id)

def results(request, question_id):
    return HttpResponse('this is result of question id: %s' % question_id)

def vote(request, question_id):
    return HttpResponse('this is vote of question id: %s' % question_id)



