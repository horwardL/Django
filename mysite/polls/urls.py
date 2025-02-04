from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    # if user go to url '' follow by it,
    # then goto views.py and call index function

    # ex: /polls/
    path('', views.IndexView.as_view(), name='index'),
    # ex: /polls/5
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # ex: /polls/5/results/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # ex: /polls/5/votes/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
