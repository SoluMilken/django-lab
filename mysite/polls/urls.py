from django.urls import path

from . import views


urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),  # run def index in views.py
    # ex: /polls/5/
    path(
        '<int:question_id>/',
        views.detail,
        name='detail',
    ),  # run def details in views.py
    # ex: /polls/5/results/
    path(
        '<int:question_id>/results/',
        views.results,
        name='results',
    ),  # run def results in views.py
    # ex: /polls/5/vote/
    path(
        '<int:question_id>/vote/',
        views.vote,
        name='vote',
    ),  # run def results in views.py
]
