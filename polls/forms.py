from django.forms import ModelForm, ModelMultipleChoiceField
from .models import Quiz, Question

# [TODO] Due to limitations in Djangos nested forms, this didn't quite work out
# as expected.

class QuizForm(ModelForm):
    questions = ModelMultipleChoiceField(queryset=Question.objects.all())

    class Meta:
        model = Quiz
        fields = "__all__"