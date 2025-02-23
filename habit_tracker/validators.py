from rest_framework.exceptions import ValidationError


class GoodHabitValidator:
    def __init__(self, good_habit, prize):
        self.good_habit = good_habit
        self.prize = prize

    def __call__(self, value):
        good_habit = dict(value).get(self.good_habit)
        prize = dict(value).get(self.prize)
        if good_habit and prize is not None:
            raise ValidationError("Одновременно нельзя указать приятную привычку и вознаграждение")


class DeadlineValidator:
    def __init__(self, deadline):
        self.deadline = deadline

    def __call__(self, value):
        deadline = dict(value).get(self.deadline)
        if int(deadline) > 120:
            raise ValidationError("Время выполнения не может быть больше 120")


class ConnectedHabitValidator:
    def __init__(self, connected_habit):
        self.connected_habit = connected_habit

    def __call__(self, value):
        connected_habit = dict(value).get(self.connected_habit)
        if connected_habit and connected_habit.good_habit is False:
            raise ValidationError("Может быть только приятная привычка")
