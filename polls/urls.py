from django.urls import path
from . import views

app_name = "polls"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"), #eg /polls/
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),#eg /polls/5/results/
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),# eg /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),# eg /polls/5/vote/
]