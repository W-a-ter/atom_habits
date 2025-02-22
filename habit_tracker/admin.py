from django.contrib import admin

from habit_tracker.models import Habit


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    """Отображает модели пользователей в админке"""

    list_display = (
        "id",
        "action",
        "user",
        "good_habit",
        "prize",
        "connected_habit",
        "period",
        "privacy",
    )
    list_filter = (
        "id",
        "user",
        "good_habit",
        "connected_habit",
        "period",
        "privacy",
    )
    search_fields = (
        "id",
        "user",
        "good_habit",
        "connected_habit",
        "period",
        "privacy",
    )
