from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import RequestContext, loader
from .models import Question, Choice


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list' : latest_question_list,
    }
    return HttpResponse(render(request, 'polls/index.html', context))


def detail(request, question_id):
    q = get_object_or_404(Question, pk=question_id)
    return HttpResponse(render(request, 'polls/detail.html', {'question': q}))


def results(request, question_id):
    return HttpResponse('this is result of question id: %s' % question_id)


def vote(request, question_id):
    return HttpResponse('this is vote of question id: %s' % question_id)



