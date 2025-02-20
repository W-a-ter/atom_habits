from rest_framework.serializers import ModelSerializer

from habit_tracker.models import Habit
from habit_tracker.validators import GoodHabitValidator, DeadlineValidator, ConnectedHabitValidator


class HabitSerializer(ModelSerializer):
    """Класс сериализатор привычки."""

    class Meta:
        model = Habit
        exclude = ('user',)
        validators = [
            GoodHabitValidator(
                good_habit='good_habit',
                prize='prize'
            ),
            DeadlineValidator(deadline='deadline'),
            ConnectedHabitValidator(connected_habit='connected_habit')
        ]


class PublishHabitSerializer(ModelSerializer):
    """Класс сериализатор пользователя."""

    class Meta:
        model = Habit
        fields = "__all__"
