from rest_framework import serializers
from .models import User, UserInfo

class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = ['phone', 'billing_address']


class UserSerializer(serializers.ModelSerializer):
    info = UserInfoSerializer()

    class Meta:
        model = User
        fields = ['id','password', 'last_login', 'is_superuser', 'username', 'first_name',
                  'last_name', 'email', 'is_staff', 'is_active', 'date_joined', 'groups', 'user_permissions', 'info']
        read_only_fields = ['is_superuser', 'is_staff', 'date_joined', 'is_active', 'user_permissions','last_login']

    def update(self, instance, validated_data):
        info_data = validated_data.pop('info')
        info = instance.info

        for field, value in validated_data.items():
            setattr(instance, field, value)
        instance.save()

        for field, value in info_data.items():
            setattr(info, field, value)
        info.save()


