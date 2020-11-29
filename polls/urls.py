from django.urls import path

from . import views

urlpatterns = [
    path('', views.QuizList.as_view(), name="index"),
    path('quiz/<int:pk>', views.QuizDetail.as_view(), name="detail"),
    path('attempts', views.AttemptsList.as_view(), name="attempts"),
    path('submit', views.submit, name="submit")
]