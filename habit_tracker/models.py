from django.db import models

# Create your models here.
class Habit(models.Model):
    user=models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="Пользователь", null=True, blank=True)
    location=models.DateTimeField(verbose_name="место выполнения привычки", null=True, blank=True)
    time=models.DateTimeField(verbose_name="время выполнения привычки", null=True, blank=True)
    action=models.TextField(verbose_name="действие", null=True, blank=True)
    good_habit=models.TextField(verbose_name="признак приятной привычки", null=True, blank=True)
    connected_habit=
    period=
    prize=
    deadline=
    privacy=

    def __str__(self):
        return f"{self.user}"

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"
