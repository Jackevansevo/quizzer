from django.conf import settings
from django.db import models

from django.urls import reverse


class Quiz(models.Model):
    title = models.TextField()

    class Meta:
        verbose_name_plural = "quizzes"

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.pk)])

    def __str__(self):
        return self.title


class Question(models.Model):
    text = models.TextField()
    # Each quiz can have multiple questions
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name="questions")

    def __str__(self):
        return self.text


class Option(models.Model):
    correct = models.BooleanField()
    text = models.TextField()
    # Question question has multiple options
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name="options"
    )

    def __str__(self):
        return self.text


class Attempt(models.Model):
    """
    Model records what user attempts at each quiz
    """

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    score = models.IntegerField()

    class Meta:
        # Each user can only attempt a quiz once
        unique_together = (
            "user",
            "quiz",
        )