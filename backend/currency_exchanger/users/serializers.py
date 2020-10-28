from rest_framework import serializers
from .models import User, UserInfo

class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = ('user', 'phone', 'billing_address')


class UserSerializer(serializers.ModelSerializer):
    info = UserInfoSerializer()
    class Meta:
        model = User
        fields = ['id','password', 'last_login', 'is_superuser', 'username', 'first_name',
                  'last_name', 'email', 'is_staff', 'is_active', 'date_joined', 'groups', 'user_permissions', 'info']

    def update(self, instance, validated_data):
        info_data = validated_data.pop('info')
        info = instance.info

        instance.password = validated_data.get('password',instance.password)
        instance.last_login = validated_data.get('last_login', instance.last_login)
        instance.is_superuser = validated_data.get('is_superuser', instance.is_superuser)
        instance.username = validated_data.get('username',instance.username)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email',instance.email)
        instance.is_staff = validated_data.get('is_staff',instance.is_staff)
        instance.is_active = validated_data.get('is_active',instance.is_active)
        instance.date_joined = validated_data.get('date_joined',instance.date_joined)
        instance.groups = validated_data.get('groups', instance.groups)
        instance.user_permissions = validated_data('user_permissions', instance.user_permissions)
        instance.save()
        info.user = info_data.get('user',info.user)
        info.phone = info_data.get('phone', info.phone)
        info.billing_address = info_data.get('billing_address', info.billing_address)
        info.save()
        return instance


