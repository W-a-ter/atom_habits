from django.db import models

from users.models import CustomUser


# Create your models here.
class Habit(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="пользователь", null=True, blank=True)
    location = models.DateTimeField(verbose_name="место выполнения привычки", null=True, blank=True)
    time = models.DateTimeField(verbose_name="время выполнения привычки", null=True, blank=True)
    action = models.TextField(verbose_name="действие", null=True, blank=True)
    good_habit = models.BooleanField(verbose_name="признак приятной привычки", null=True, blank=True)
    connected_habit = models.ForeignKey(
        "habit_tracker.Habit", on_delete=models.CASCADE, verbose_name="связанная привычка", null=True, blank=True
    )
    period = models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7)], default=1)
    prize = models.TextField(verbose_name="Приз", null=True, blank=True)
    deadline = models.PositiveIntegerField(verbose_name="время на выполнение", null=True, blank=True)
    privacy = models.BooleanField(verbose_name="приватность", null=True, blank=True)

    def __str__(self):
        return f"{self.user}"

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"
