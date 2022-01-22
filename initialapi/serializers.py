import re

from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

        extra_kwargs = {
            'password': {
                'write_only': True
             },
            'email': {
                'required': True
            }
        }

    def validate_password(self, value: str):
        length_error = len(value) < 8
        digit_error = re.search(r"\d", value) is None
        uppercase_error = re.search(r"[A-Z]", value) is None
        lowercase_error = re.search(r"[a-z]", value) is None
        symbol_error = re.search(r"[ !#$%&'()*+,-./[\\\]^_`{|}~" + r'"]', value) is None

        if length_error:
            raise serializers.ValidationError('password must contain 8 symbols')
        elif digit_error:
            raise serializers.ValidationError('password must contain digits')
        elif lowercase_error:
            raise serializers.ValidationError('password must contain at least one lowercase latter')
        elif uppercase_error:
            raise serializers.ValidationError('password must contain at least one uppercase latter')
        elif symbol_error:
            raise serializers.ValidationError('password must contain at least one punctuation latter')

        return value
