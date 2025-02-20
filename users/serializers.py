from rest_framework.serializers import ModelSerializer

from users.models import CustomUser


class UserSerializer(ModelSerializer):
    """Класс сериализатор пользователя."""

    class Meta:
        model = CustomUser
        fields = ("username", "tg_chat_id")
