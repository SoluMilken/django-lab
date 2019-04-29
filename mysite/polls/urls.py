from django.urls import path

from . import views


app_name = 'polls'  # add namespaces to URLconf
urlpatterns = [
    # ex: /polls/
    path(
        '',
        views.IndexView.as_view(),
        name='index',
    ),  # run def index in views.py
    # ex: /polls/5/
    path(
        '<int:pk>/',
        views.DetailView.as_view(),
        name='detail',
    ),  # run def details in views.py
    # ex: /polls/5/results/
    path(
        '<int:pk>/results/',
        views.ResultsView.as_view(),
        name='results',
    ),  # run def results in views.py
    # ex: /polls/5/vote/
    path(
        '<int:question_id>/vote/',
        views.vote,
        name='vote',
    ),  # run def results in views.py
]
