from .models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields=('first_name','last_name','father_name','gender','email','phone','spouse_name')
