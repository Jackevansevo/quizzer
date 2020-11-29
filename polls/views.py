from django.views.generic import DetailView, ListView
from .models import Quiz, Attempt
from .forms import QuizForm

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.shortcuts import reverse, redirect


@login_required
@require_POST
def submit(request):
    quiz_id = request.POST.get('quiz')[0]
    quiz = Quiz.objects.get(id=quiz_id)
    score = 0
    for question in quiz.questions.all():
        # Look up submitted answer in the request
        answers = set(request.POST.getlist(str(question.id)))
        correct = set(question.options.filter(correct=True).values_list('text', flat=True))
        if correct == answers:
            score+=1
    Attempt.objects.create(quiz=quiz, user=request.user, score=score)
    return redirect(reverse("index"))


class QuizList(ListView):
    model = Quiz


class QuizDetail(LoginRequiredMixin, DetailView):
    model = Quiz


class AttemptsList(LoginRequiredMixin, ListView):
    model = Attempt

    def get_queryset(self):
        queryset = super(AttemptsList, self).get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset