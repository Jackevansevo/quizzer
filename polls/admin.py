from django.contrib import admin

from .models import Quiz, Question, Attempt, Option

class QuestionsInline(admin.TabularInline):
    model = Question
    fields = ("text",)


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    inlines = (QuestionsInline,)


@admin.register(Attempt)
class AttemptAdmin(admin.ModelAdmin):
    pass


@admin.register(Option)
class OptionAdmin(admin.ModelAdmin):
    pass


class OptionsInline(admin.TabularInline):
    model = Option
    fields = ("text", "correct")


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = (OptionsInline,)
