from rest_framework.serializers import ModelSerializer
# from models import User

from django.contrib.auth.models import User


class UserSerilizer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email']
