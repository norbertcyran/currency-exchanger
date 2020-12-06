from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers

from .models import User, UserInfo


class CustomRegisterSerializer(RegisterSerializer):
    first_name = serializers.CharField(required=True, write_only=True)
    last_name = serializers.CharField(required=True, write_only=True)
    billing_address = serializers.CharField(required=True, write_only=True)
    phone = serializers.CharField(required=True, write_only=True)

    def custom_signup(self, validated_data, user):
        profile = UserInfo.objects.create(user=user)
        user.first_name = self.validated_data.get("first_name", "")
        user.last_name = self.validated_data.get("last_name", "")
        profile.billing_address = self.validated_data.get("billing_address", "")
        profile.phone = self.validated_data.get("phone", "")
        profile.save()
        user.save()


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = ["phone", "billing_address"]


class UserSerializer(serializers.ModelSerializer):
    info = UserInfoSerializer()

    class Meta:
        model = User
        fields = [
            "id",
            "last_login",
            "is_superuser",
            "username",
            "first_name",
            "last_name",
            "email",
            "is_staff",
            "is_active",
            "date_joined",
            "info",
        ]
        read_only_fields = [
            "is_superuser",
            "is_staff",
            "date_joined",
            "is_active",
            "last_login",
        ]

    def update(self, instance, validated_data):
        info_data = validated_data.pop("info")
        info = instance.info

        for field, value in validated_data.items():
            setattr(instance, field, value)
        instance.save()

        for field, value in info_data.items():
            setattr(info, field, value)
        info.save()
