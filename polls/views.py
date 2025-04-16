from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Question

# Create your views here.
#create an index view for the polls app with httpresponse
#import the question model
#import from django http  http404
#import get obejct from shortcuts

#create a view to show the latest questions
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request,"polls/index.html", context)

#create a view to show details of a question when selected
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})

#create a view to show the results of a question
def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

#create a view to enable voting on a question
def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)